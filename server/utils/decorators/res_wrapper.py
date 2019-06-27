from functools import wraps
from flask import make_response, jsonify
from ..exception.exception import APIException, ServerException


def resp_success(**kwargs):
    return make_response(jsonify({
        'status': 0,
        'msg': kwargs.get('msg') or '成功',
        'data': kwargs.get('data') or None
    }), kwargs.get('code') or 200)

def resp_api_error(**kwargs):
    return make_response(jsonify({
        'status': -1,
        'msg': kwargs.get('msg') or '请求无效',
        'data': None
    }), kwargs.get('code') or 400)

def resp_server_error(**kwargs):
    return jsonify({
        'status': -1,
        'msg': kwargs.get('msg') or '服务端错误',
        'data': None
    }, kwargs.get('code') or 500)

def resp_wrapper(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return resp_success(**func(*args, **kwargs))
        except APIException as apiExc:
            return resp_api_error(**{ 'msg': apiExc.msg, 'code': apiExc.code })
        except ServerException as serverExc:
            return resp_server_error(**{ 'msg': apiExc.msg, 'code': apiExc.code })
        else:
            return resp_success()
    return decorator
