__version__ = '0.1.0'

from os import getenv

def get_environment(variable, default=None, encoding='utf-8'):
    """Get value of an environment variable.
    
    Returns the value of an environment variable if it exists.
    If it does not exist and a {name}_FILE variable exists, the content of the
    file it points to will be returned.
    If neither exist, it returns the supplied default argument.
    
    Args:
        name (str): Name of the environment variable based option.
        default (str): Default option, returned when the variable does not exist.
    Returns:
        str: Value of the variable, or content of {name}_FILE file.
    """
    if value := getenv(variable):
        return value
    elif file := getenv(f'{variable}_FILE'):
        return open(file, mode='r', encoding=encoding).read()
    else:
        return default
