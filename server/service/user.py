import os, binascii

from flask import make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from server.utils.exception.exception import APIException
from server.utils.decorators.json_required import json_required
from server.utils.decorators.commit import commit
from server.dao.user import User
from server.dao.session import Session

def generateSessionId():
    return binascii.b2a_base64(os.urandom(24))[:-1] 

def insertSessionId(session_id):
    return Session.insert(session_id=session_id)

def generateAndInsertSessionId():
    return insertSessionId(generateSessionId())

@commit
@json_required
def userRegister(params):
    username = params.get('username')
    password = params.get('password')

    if username is None or password is None:
        raise APIException('用户名或密码不能为空', 400)
    if User.queryByUserName(username) is not None:
        raise APIException('该用户已存在，请登录', 200)
    
    password_hash = generate_password_hash(password)
    User.insert(username=username, password=password_hash)

    return {
        'msg': '注册成功'
    }

@commit
@json_required
def userLogin(params, cookies):
    username = params.get('username')
    password = params.get('password')

    if username is None or password is None:
        raise APIException('用户名或密码不能为空', 400)
    
    user = User.queryByUserName(username)

    if user is None:
        raise APIException('该用户不存在，请注册', 200)
    if check_password_hash(user.password, password) is False:
        raise APIException('密码不正确', 200)

    user_session_id = cookies.get('USER_SESSION')

    if user_session_id is None or user_session_id is not None and Session.queryBySessionId(user_session_id) is None:
        if generateAndInsertSessionId() is None:
            raise APIException('用户登录异常', 401)
    
    return {
        'msg': '登录成功'
    }