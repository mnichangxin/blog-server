from functools import wraps
from flask import request
from server.utils.exception.exception import APIException, ServerException

def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        return func(*args, **kwargs)
    return decorator