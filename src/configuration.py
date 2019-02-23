import os


def get_environment_value(key):
    value = os.environ[key]
    if value is None:
        raise ValueError('A {} is not found in the os environment variables.'.format(key))
    return value


def get_url():
    return get_environment_value('TARGET_URL')


def get_log_level():
    try:
        return get_environment_value('LOG_LEVEL')
    except:
        return 'INFO'

