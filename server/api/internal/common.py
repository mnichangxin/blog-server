from flask import Blueprint, request
from ...utils.decorators.res_wrapper import resp_wrapper
from ...service.common import post_publish, post_query

internal = Blueprint('internal', __name__)

@internal.route('/post_publish', methods=['POST'])
@resp_wrapper
def api_post_publish():
    return post_publish(request.get_json())

@internal.route('/post_query', methods=['GET'])
@resp_wrapper
def api_post_query():
    return post_query(request.get_json())