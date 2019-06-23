from functools import wraps
from flask import jsonify
from ..exception.exception import APIException, ServerException

def resp_wrapper(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except APIException as apiExc:
            return jsonify({
                'msg': 'API 异常'
            })
        except ServerException as serverExc:
            return jsonify({
                'msg': '服务端错误'
            })
    return decorator
