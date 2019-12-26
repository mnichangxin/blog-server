import logging

from functools import wraps
from flask import make_response, jsonify, Response
from server.utils.exception.exception import APIException, ServerException

def combine_response(**kwargs):
    res_default = { 'status': 0, 'msg': '成功', 'data': None }
    return jsonify({ **res_default, **kwargs })

def resp_wrapper(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            response_func = func(*args, **kwargs)
            if isinstance(response_func, Response):
                return response_func
            else:
                return make_response(combine_response(**response_func), kwargs.get('code') or 200)
        except APIException as apiExc:
            return make_response(combine_response(**{ 'status': -1, 'msg': apiExc.msg }), apiExc.code or 400)
        except ServerException as serverExc:
            return make_response(combine_response(**{ 'status': -1, 'msg': apiExc.msg }), apiExc,code or 500)
        except Exception as unkownExc:
            logging.error(unkownExc)
            return make_response(combine_response(**{ 'status': -1, 'msg': '服务端错误' }), apiExc.code or 500)
    return decorator
