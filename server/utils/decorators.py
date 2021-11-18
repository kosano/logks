from functools import wraps
import logging

logger = logging.getLogger(__name__)


def if_error_or(default=None, exp=Exception):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exp as e:
                logger.error(
                    f'function: {func.__name__} failure. message: {e}')
                return default
        return wrapped
    return decorator
