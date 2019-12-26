from functools import wraps
from flask import request
from server.utils.exception.exception import APIException, ServerException
from server.service.user import checkLoginStatus

def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        cookies = request.cookies
        if not checkLoginStatus(cookies):
            raise APIException('用户未登录', 403)
        return func(*args, **kwargs)
    return decorator