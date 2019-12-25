from flask import Blueprint, request
from server.utils.decorators.res_wrapper import resp_wrapper
from server.service.user import userRegister, userLogin, userLogout

bp = Blueprint('user', __name__, url_prefix='/v1/internal/user')

@bp.route('/register', methods=['POST'])
@resp_wrapper
def user_register():
    return userRegister(request.get_json())

@bp.route('login', methods=['POST'])
@resp_wrapper
def user_login():
    return userLogin(request.get_json(), request.cookies)

@bp.route('logout', methods=['GET', 'POST'])
@resp_wrapper
def user_logout():
    return userLogout(request.cookies) 