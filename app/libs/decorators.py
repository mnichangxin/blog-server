from functools import wraps
from .error import APIException

def resp_wrapper(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise APIException('服务端异常', 500)
    return decorator
