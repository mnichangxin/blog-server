from flask import Blueprint, request
from server.utils.decorators.res_wrapper import resp_wrapper
from server.utils.decorators.login_required import login_required
from server.utils.decorators.json_required import json_required
from server.service.post import postPublish, postQuery, postDelete, postUpdate
from server.service.file import fileUpload


bp = Blueprint('posts', __name__, url_prefix='/v1/view/post')

@bp.route('/query', methods=['GET'])
@resp_wrapper
@json_required
def post_query():
    return postQuery(request.get_json())