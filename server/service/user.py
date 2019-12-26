import os, binascii

from flask import make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from server.utils.exception.exception import APIException
from server.utils.decorators.commit import commit
from server.dao.user import User
from server.dao.session import Session

def generateSessionId():
    return binascii.b2a_base64(os.urandom(24))[:-1] 

def setCookies(response, res_cookies):
    for i in res_cookies:
        response.set_cookie(i, res_cookies[i])

def checkLoginStatus(cookies):
    login_status = False
    user_session_id = cookies.get('USER_SESSION')
    if user_session_id is not None and Session.queryBySessionId(user_session_id) is not None:
        login_status = True
    return login_status

@commit
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
        user_session_id = generateSessionId()
        if Session.insert(session_id=user_session_id) is None:
            raise APIException('用户登录异常', 401)

    res = make_response(jsonify({ 'status': 0, 'msg': '登录成功', 'data': None }), 200)
    res_cookies = cookies.__dict__
    res_cookies['USER_SESSION'] = user_session_id
    setCookies(res, res_cookies)

    return res

@commit
def userLogout(cookies):
    user_session_id = cookies.get('USER_SESSION')
    
    if user_session_id is None or user_session_id is not None and Session.queryBySessionId(user_session_id) is None:
        raise APIException('用户已登出', 200)
    
    Session.deleteBySessionId(session_id=user_session_id)

    res = make_response(jsonify({ 'status': 0, 'msg': '登出成功', 'data': None }), 200)
    res.delete_cookie('USER_SESSION')

    return res

@commit
def checkLogin(cookies):
    res = { 'msg': '用户未登录', 'loginStatus': False }
    if checkLoginStatus(cookies):
        res['msg'] = '用户已登录'
        res['loginStatus'] = True
    return res
