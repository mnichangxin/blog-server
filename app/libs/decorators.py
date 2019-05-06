from functools import wraps
from .error import APIException

def resp_wrapper(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return 'Unknown mistake'
    return decorator
