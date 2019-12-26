from flask import Blueprint, request
from server.utils.decorators.res_wrapper import resp_wrapper
from server.utils.decorators.json_required import json_required
from server.service.user import userRegister, userLogin, userLogout, checkLogin

bp = Blueprint('user', __name__, url_prefix='/v1/internal/user')

@bp.route('/register', methods=['POST'])
@resp_wrapper
@json_required
def user_register():
    return userRegister(request.get_json())

@bp.route('/login', methods=['POST'])
@resp_wrapper
@json_required
def user_login():
    return userLogin(request.get_json(), request.cookies)

@bp.route('/logout', methods=['GET', 'POST'])
@resp_wrapper
def user_logout():
    return userLogout(request.cookies) 

@bp.route('/checkLogin', methods=['GET', 'POST'])
@resp_wrapper
def check_login():
    return checkLogin(request.cookies)