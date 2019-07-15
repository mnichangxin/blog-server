from flask import Blueprint, request
from ...utils.decorators.res_wrapper import resp_wrapper
from ...service.common import post_publish

internal = Blueprint('internal', __name__)

@internal.route('/post_publish', methods=['POST'])
@resp_wrapper
def post_publish():
    return post_publish(request.get_json())