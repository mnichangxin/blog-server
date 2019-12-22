from werkzeug.security import generate_password_hash
from server.utils.exception.exception import APIException
from server.utils.decorators.json_required import json_required
from server.utils.decorators.commit import commit
from server.dao.user import User

@commit
@json_required
def register(params):
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
