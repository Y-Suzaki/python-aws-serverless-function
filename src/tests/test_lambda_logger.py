from unittest import TestCase
from logger import LambdaLogger


class TestLambdaLogger(TestCase):
    def setUp(self):
        self.logger = LambdaLogger('DEBUG')

    def test_debug(self):
        self.logger.debug('This message is DEBUG level.')

    def test_info(self):
        self.logger.info('This message is INFO level.')
        self.logger.info('This message is INFO level.', '0001')

    def test_warning(self):
        self.logger.warning('This message is WARNING level.', '0002')

    def test_error(self):
        self.logger.error('This message is ERROR level.', '0003')

    def test_exception(self):
        try:
            raise Exception('Internal server error.')
        except:
            self.logger.exception('This message is ERROR(Exception) level.', '0004')
