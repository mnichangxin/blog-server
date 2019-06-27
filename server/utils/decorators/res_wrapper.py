from functools import wraps
from flask import make_response, jsonify
from ..exception.exception import APIException, ServerException


def resp_success(*args, **kwargs):
    return make_response(jsonify({
        'status': 0,
        'msg': '成功',
        'data': kwargs['data']
    }), 200)

def resp_api_error(*args, **kwargs):
    return make_response(jsonify({
        'status': -1,
        'msg': kwargs['msg'],
        'data': None
    }), kwargs['code'])

def resp_server_error(*args, **kwargs):
    return jsonify({
        'status': -1,
        'msg': kwargs['msg'],
        'data': None
    }, kwargs['code'])

def resp_wrapper(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return resp_success(data=func(*args, **kwargs))
        except APIException as apiExc:
            return resp_api_error(**{ 'msg': apiExc.msg, 'code': apiExc.code })
        except ServerException as serverExc:
            return resp_server_error(**{ 'msg': apiExc.msg, 'code': apiExc.code })
        else:
            return resp_success()
    return decorator
