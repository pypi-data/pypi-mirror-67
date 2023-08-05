import json

import jsonschema


JSON_SCHEMA = {
    'type': 'object',
    'properties': {
        'corpus': {
            'type': 'object',
            'properties': {
                'directories': {
                    'type': 'array',
                    'items': {'type': 'string'}
                },
                'connections': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string'},
                            'driver': {'type': 'string'},
                            'server': {'type': 'string'},
                            'database': {'type': 'string'},
                            'name_col': {'type': 'string'},
                            'text_col': {'type': 'string'}
                        }
                    }
                },
            }
        },
        'keywords': {  # paths to keyword files
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'path': {'type': 'string'},
                    'regex_variation': {'type': 'integer'},  # -1 to 3
                    'word_order': {'type': 'integer'},
                    'max_search': {'type': 'integer'},
                    'max_intervening': {'type': 'integer'},
                }
            }
        },
        'negation': {
            'type': 'object',
            'properties': {
                'version': {'type': 'integer'},  # built-in version
                'path': {'type': 'string'},
                'skip': {'type': 'boolean'},
                'variation': {'type': 'integer'},
            }
        },
        'output': {
            'type': 'object',
            'properties': {
                'outfile': {'type': 'string'},
                'path': {'type': 'string'},
                'hostname': {'type': 'string'},
            }
        },
        'logger': {
            'type': 'object',
            'properties': {
                'verbose': {'type': 'boolean'}
            }
        }
    }
}


def myexec(code):
    import warnings
    warnings.warn('Executing python external file: only do this if you trust it')
    import sys
    from io import StringIO
    temp_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        # try if this is a expression
        ret = eval(code)
        result = sys.stdout.getvalue()
        if ret:
            result = result + ret
    except:
        try:
            exec(code)
        except:
            # you can use <traceback> module here
            import traceback
            buf = StringIO()
            traceback.print_exc(file=buf)
            error = buf.getvalue()
            raise ValueError(error)
        else:
            result = sys.stdout.getvalue()
    sys.stdout = temp_stdout
    return result


def load_yaml(fh):
    try:
        import yaml  # pyyaml
    except ModuleNotFoundError:
        try:
            from ruamel import yaml
        except ModuleNotFoundError:
            raise ModuleNotFoundError('Missing module: `yaml`. Install pyyaml or ruamel.yaml from pip.')
    return yaml.load(fh)


def get_config(path):
    with open(path) as fh:
        if path.endswith('json'):
            return json.load(fh)
        elif path.endswith('yaml'):
            return load_yaml(fh)
        elif path.endswith('py'):
            return eval(myexec(fh.read()))
        else:
            raise ValueError('Unrecognized configuration file type: {}'.format(path.split('.')[-1]))


def validate_config(path):
    conf = get_config(path)
    jsonschema.validate(conf, JSON_SCHEMA)
    return conf
