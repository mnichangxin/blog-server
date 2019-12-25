from flask import Blueprint, request
from server.utils.decorators.res_wrapper import resp_wrapper
from server.utils.decorators.login_required import login_required
from server.utils.decorators.json_required import json_required
from server.service.post import postPublish, postQuery, postDelete, postUpdate
from server.service.file import fileUpload

bp = Blueprint('post', __name__, url_prefix='/v1/internal/post')

@bp.route('/publish', methods=['POST'])
@resp_wrapper
@login_required
@json_required
def post_publish():
    return postPublish(request.get_json())

@bp.route('/query', methods=['GET'])
@resp_wrapper
@login_required
@json_required
def post_query():
    return postQuery(request.get_json())

@bp.route('/delete', methods=['POST'])
@resp_wrapper
@login_required
@json_required
def post_delete():
    return postDelete(request.get_json())

@bp.route('/update', methods=['POST'])
@resp_wrapper
@login_required
@json_required
def post_update():
    return postUpdate(request.get_json())

@bp.route('/fileUpload', methods=['POST'])
@resp_wrapper
@login_required
def file_upload():
    return fileUpload(request.files)