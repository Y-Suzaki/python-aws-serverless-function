"""
ヘルスチェックの機能を提供するモジュールです。
"""
from interceptor import trace_interceptor
from logger import LambdaLogger
from configuration import get_url
import requests


@trace_interceptor
def health_check(event, context):
    """ ヘルスチェックを実施します。
    失敗と判断する場合は、必ずExceptionをraiseするようにしてください。
    :param event:
    :param context:
    """
    url = get_url()
    logger = LambdaLogger.get_logger()

    # 以下にヘルスチェックを実装する
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Http status code of the response is not equal 200.')
