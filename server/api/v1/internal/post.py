from flask import Blueprint, request
from server.utils.decorators.res_wrapper import resp_wrapper
from server.service.common import post_publish, post_query, post_delete, post_update

bp = Blueprint('post', __name__, url_prefix='/v1/internal/post')

@bp.route('/publish', methods=['POST'])
@resp_wrapper
def post_publish():
    return post_publish(request.get_json())

@bp.route('/query', methods=['GET'])
@resp_wrapper
def post_query():
    return post_query(request.get_json())

@bp.route('/delete', methods=['POST'])
@resp_wrapper
def post_delete():
    return post_delete(request.get_json())

@bp.route('/update', methods=['POST'])
@resp_wrapper
def post_update():
    return post_update(request.get_json())