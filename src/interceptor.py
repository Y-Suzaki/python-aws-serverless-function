from logger import LambdaLogger


def trace_interceptor(func):
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = LambdaLogger.get_logger()
        try:
            logger.info('Health check started.', 'I0001')
            func(*args, **kwargs)
            logger.info('Health check succeeded.', 'I0002')
        except Exception:
            logger.exception('Health check failed, please check the target application.', 'E0001')
    return wrapper
