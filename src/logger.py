"""
ロギングの機能を提供するモジュールです。
ログフォーマットの統一のため、本ロギングを使用してください。
"""
from logging import getLogger, getLevelName, StreamHandler, Formatter
from configuration import get_log_level
import time


class LambdaLogger:
    """ Lambda用のロガーです。
    """
    @staticmethod
    def get_logger():
        """ ロガーを取得します。
        """
        return LambdaLogger(get_log_level())

    def __init__(self, level_name):
        """ ログフォーマットの指定をします。
        :param level_name: ログレベル
        """
        level = getLevelName(level_name)
        self.logger = getLogger()
        self.logger.setLevel(level)

        formatter = Formatter(
            '%(levelname)s %(error_code)s %(asctime)s %(message)s', '%Y-%m-%dT%H:%M:%SZ')
        formatter.converter = time.gmtime

        if self.logger.handlers:
            for handler in self.logger.handlers:
                handler.setFormatter(formatter)
        else:
            handler = StreamHandler()
            handler.setLevel(level)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def debug(self, message, error_code='-'):
        self.logger.debug(message, extra={'error_code': error_code})

    def info(self, message, error_code='-'):
        self.logger.info(message, extra={'error_code': error_code})

    def warning(self, message, error_code):
        self.logger.warning(message, extra={'error_code': error_code})

    def error(self, message, error_code):
        self.logger.error(message, extra={'error_code': error_code})

    def exception(self, message, error_code):
        self.logger.exception(message, extra={'error_code': error_code})
