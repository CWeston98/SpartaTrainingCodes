import configparser

_config = configparser.ConfigParser()
_config.read('config/config.ini')


def find_var_rabbit(variable):
    return _config['RABBIT'][variable]


def find_var_hawk(variable):
    return _config['HAWK'][variable]
