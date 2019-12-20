from flask import Blueprint, request
from server.utils.decorators.res_wrapper import resp_wrapper
from server.service.post import postPublish, postQuery, postDelete, postUpdate
from server.service.file import fileUpload

bp = Blueprint('post', __name__, url_prefix='/v1/internal/post')

@bp.route('/publish', methods=['POST'])
@resp_wrapper
def post_publish():
    return postPublish(request.get_json())

@bp.route('/query', methods=['GET'])
@resp_wrapper
def post_query():
    return postQuery(request.get_json())

@bp.route('/delete', methods=['POST'])
@resp_wrapper
def post_delete():
    return postDelete(request.get_json())

@bp.route('/update', methods=['POST'])
@resp_wrapper
def post_update():
    return postUpdate(request.get_json())

@bp.route('/fileUpload', methods=['POST'])
@resp_wrapper
def file_upload():
    return fileUpload(request.files)