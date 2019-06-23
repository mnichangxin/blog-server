from flask import Blueprint, request
from ...utils.decorators.res_wrapper import resp_wrapper
from ...service

admin = Blueprint('admin', __name__)

@admin.route('/publish', methods=['POST'])
@resp_wrapper
def publish():
    params = request.get_json()
    return Post().insertPost(params)