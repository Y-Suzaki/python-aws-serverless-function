"""
環境設定の機能を提供するモジュールです。
"""
import os


def get_environment_value(key):
    """ 環境変数を取得します。
    :param key: 環境変数の名前
    :return: 環境変数の値
    """
    value = os.environ[key]
    if value is None:
        raise ValueError('A {} is not found in the os environment variables.'.format(key))
    return value


def get_url():
    """ 環境変数からURLを取得します。
    :return: URL
    """
    return get_environment_value('TARGET_URL')


def get_log_level():
    """ 環境変数からログレベルを取得します。
    :return: ログレベル
    """
    try:
        return get_environment_value('LOG_LEVEL')
    except:
        return 'INFO'

