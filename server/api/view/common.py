from flask import Blueprint, jsonify
from ...service.common import post_query
from ...utils.decorators.res_wrapper import resp_wrapper

view = Blueprint('view', __name__)

@view.route('/post_query', methods=['GET'])
@resp_wrapper
def post_query():
    return post_query(request.get_json())