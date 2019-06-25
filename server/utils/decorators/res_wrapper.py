from functools import wraps
from flask import jsonify
from ..exception.exception import APIException, ServerException


def resp_success():
    return jsonify({
        'status': 0,
        'msg': '成功',
        'data': []
    })

def resp_api_error(msg):
    return jsonify({
        'status': -1,
        'msg': msg,
        'data': None
    })

def resp_server_error(msg):
    return jsonify({
        'status': -1,
        'msg': '服务端错误',
        'data': None
    })

def resp_wrapper(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except APIException as apiExc:
            return resp_api_error(apiExc.msg)
        except ServerException as serverExc:
            return resp_server_error()
        else:
            return resp_success()
    return decorator
