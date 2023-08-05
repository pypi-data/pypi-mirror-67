import argparse
import csv
import logging
import logging.config
import os

from pytakes.dict.rules import read_file, read_rules, generate_combinations, build_rows
from pytakes.dict.rules import read_files
from pytakes.util import mylogger
from pytakes.util.db_reader import DbInterface
from pytakes.util.utils import get_valid_args


def check_if_table_exists(db, table_name):
    if db.is_sql_server_connection():
        return db.execute_fetchone('''
                    IF EXISTS (SELECT *
                               FROM INFORMATION_SCHEMA.TABLES
                               WHERE TABLE_NAME = '%s')
                      SELECT COUNT(*)
                        FROM %s
                    ELSE
                      SELECT -1
                    ''' % (table_name, table_name)
                                   )[0]
    else:  # unknown connection type: assume table doesn't exist
        logging.warning('Untested database connection: Connection is not SQL Server.')
        logging.warning('Assuming table "{}" does not exist. If it does exist, '
                        'delete it and restart the process.'.format(table_name))
        return -1


def drop_table(db, table_name):
    db.execute_commit('DROP TABLE %s;' % table_name)


def create_table(db, table_name):
    db.execute_commit('''
        CREATE TABLE %s
          (
            ID int,
            CUI varchar(15),
            Fword varchar(80),
            Text varchar(8000),
            Code varchar(45),
            SourceType varchar(45),
            TUI varchar(6),
            TextLength int,
            RegexVariation int,
            WordOrder int,
            Valence int
          )
    ''' % table_name)


def add_rows_to_db(rows, db, table_name):
    for num, (cui, fword, text, textlength, code, rxVar, wdOrder, val) in enumerate(rows):
        try:
            db.execute_commit('''
            INSERT INTO {} (ID, CUI, Fword, Text, TextLength, Code, SourceType, TUI, RegexVariation, WordOrder, Valence)
            VALUES ({}, '{}', '{}', '{}', {}, '{}', 'Custom', 'T033', {}, {}, {})
            '''.format(table_name, num, cui,
                       fword.replace("'", "''"), text.replace("'", "''"),
                       textlength, code, rxVar,
                       wdOrder, val))
        except Exception as e:
            return cui, fword, text, textlength, code, rxVar, wdOrder, val, str(e)
    return None


def add_rows_to_csv(rows, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['ID', 'CUI', 'Fword', 'Text', 'TextLength', 'Code', 'RegexVariation', 'WordOrder', 'Valence', 'SourceType',
             'TUI'])
        for num, row in enumerate(rows):
            writer.writerow([num] + row + ['Custom', 'T033'])
    return True


class Generator(object):
    def __init__(self):
        self.cuis = set()
        self.cui_idx = 0
        self.codes = set()
        self.code_idx = 1

    def used_cuis(self, cuis):
        for cui in cuis:
            self.used_cui(cui)

    def used_cui(self, cui):
        self.cuis.add(cui)

    def used_codes(self, codes):
        for code in codes:
            self.used_code(code)

    def used_code(self, code):
        self.codes.add(code)

    def generate_cui(self):
        while True:
            new_cui = 'G%07d' % self.cui_idx
            self.cui_idx += 1
            if new_cui in self.cuis:
                continue
            else:
                return new_cui

    def generate_code(self):
        while True:
            new_code = '1%08d' % self.code_idx
            self.code_idx += 1
            if new_code in self.codes:
                continue
            else:
                return new_code


def create_sample_directory(path=None):
    if not path:
        path = ''
    d = os.path.join(path, 'cat')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'categories.txt'), 'w') as out:
        out.write('[good]\nSuperman\nBatman\n[evil]\n\nLoki\nTwo-Face||Two Face\n')
    with open(os.path.join(path, 'rules.txt'), 'w') as out:
        out.write('[good] vs [evil]\n[good] is a good guy\n[evil] is a villain\n')
    logging.info('Created sample directory structure.')


def build(path=None, output=None, table=None, driver=None, server=None, database=None,
          ignore_categories=None):
    cwd = path
    while not path:
        cwd = input('Parent directory of files: ')
        try:
            os.chdir(cwd)
        except Exception as e:
            logging.exception(e)
            logging.error('Failed to find directory "{}".'.format(cwd))
            path = None  # reset path so user gets prompt

    logging.info('Current directory: {}.'.format(cwd))
    generator = Generator()

    # try to find the rules and categories files
    files = os.listdir(cwd)

    categories = {}
    if ignore_categories:
        logging.info('Ignoring category files.')
    else:
        cat_dir = os.path.join(cwd, 'cat')
        if 'cat' in files:
            if os.path.isdir(cat_dir):
                logging.info('Found \'cat\' directory.')
                read_files([os.path.join(cat_dir, x) for x in os.listdir(cat_dir)], categories)
            else:
                read_file(cat_dir, categories)
        else:
            for file in files:
                file = os.path.join(cwd, file)
                if os.path.splitext(file)[1] == '.cat':
                    read_file(file, categories)
                    logging.info('Found category file: %s.' % file)
        logging.info('Found {} categories.'.format(len(categories)))

        if len(categories) == 0:
            ans = input('No categories were found, would you like\n' +
                        'an example created in your current directory? (Y/n) ')
            if ans.lower() in ['y', 'yes', 'ye']:
                create_sample_directory()
            logging.error('Could not find a category file. Terminating.')
            logging.info('If you are not using categories, consider using the "--ignore-categories" flag.')
            return

    rules = []
    for file in files:
        file = os.path.join(cwd, file)
        if os.path.splitext(os.path.split(file)[1])[0] == 'rules':
            rules += read_rules(file, generator)
            logging.info('Found rule file: %s.' % file)
    logging.info('Found %d rules.' % len(rules))

    if len(rules) == 0:
        logging.info('Please create a rules files (e.g., "rules.txt").')
        logging.info('Could not find any rules. Terminating.')
        return

    logging.info('Generating combinations.')
    combos = generate_combinations(rules, categories, generator)
    rows = build_rows(combos, generator)

    # option to create csv_file
    if output:
        csv_filename = output
    else:
        csv_filename = input('CSV filename (press enter to skip): ')

    if csv_filename:
        if csv_filename[-4:] != '.csv':
            csv_filename += '.csv'
        logging.info('Outputting rows to CSV: %s.' % csv_filename)
        add_rows_to_csv(rows, os.path.join(cwd, csv_filename))

    if table:
        newtable = table
    else:
        newtable = input('SQL Server table name (press enter to skip): ')
    if newtable:
        if not server and not database:
            logging.info('No database configuration specified for new table.')
            d = input('Specify driver for new table (press enter for default "{}")'.format(driver))
            if d:
                driver = d
        if not server:
            server = input('Specify server for new table: ')
        if not database:
            database = input('Specify database for new table: ')
        db = DbInterface(driver, server, database)
        while True:
            cnt = check_if_table_exists(db, newtable)
            if cnt >= 0:
                ans = input(('Table %s already exists with %d rows.\n' +
                             'Are you sure you want to drop and recreate\n' +
                             '%s? (Y/n) ') % (newtable, cnt, newtable))
                if ans.lower() not in ['y', 'yes', 'ye']:
                    # logic for 'no' answer
                    newtable = input('SQL Server table name (press enter to skip): ')
                    continue
                else:
                    logging.info('Dropping table %s.' % newtable)
                    try:
                        drop_table(db, newtable)
                    except Exception as e:
                        logging.exception('Exception while attempting to drop table.')
                        logging.exception(e)
                        raise e
            break
        try:
            create_table(db, newtable)
        except Exception as e:
            logging.exception('Exception while attempting to drop table.')
            logging.exception(e)
            raise e
        logging.info('Adding rows to table %s.' % newtable)
        res = add_rows_to_db(rows, db, newtable)
        if res:
            row_elements = [str(x) for x in res]
            exc_text = 'Exception while adding row: %s.' % ', '.join(row_elements)
            logging.exception(exc_text)
            raise Exception(exc_text)
    logging.info('Process completed successfully.')


def main():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument('-p', '--path', default=None, help='Parent directory of folders.')
    parser.add_argument('-o', '--output', default=None, help='Output csv file.')
    parser.add_argument('-t', '--table', default=None, help='Output database table.')
    parser.add_argument('--driver', default='SQL Server', help='Driver for database connection (if needed).')
    parser.add_argument('--server', default=None, help='Server for database connection (if needed).')
    parser.add_argument('--database', default=None, help='Database for database connection (if needed).')
    parser.add_argument('--create-sample', default=None, action='store_true', help='Create sample directory.')
    parser.add_argument('--ignore-categories', action='store_true', default=False,
                        help='Do not look for cat files (categories).')

    parser.add_argument('-v', '--verbosity', type=int, default=2, help='Verbosity of log output.')
    args = parser.parse_args()

    loglevel = mylogger.resolve_verbosity(args.verbosity)
    logging.config.dictConfig(mylogger.setup('builder', logdir=args.path, loglevel=loglevel))

    if args.create_sample:
        create_sample_directory(args.path)
    else:
        try:
            build(**get_valid_args(build, vars(args)))
        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':
    main()
