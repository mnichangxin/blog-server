from flask import Blueprint, request
from server.utils.decorators.res_wrapper import resp_wrapper
from server.utils.decorators.json_required import json_required
from server.service.post import postQuery, postQueryByCategory, postQueryByTag, postQueryDetail


bp = Blueprint('posts', __name__, url_prefix='/v1/view/post')

@bp.route('/query', methods=['GET'])
@resp_wrapper
@json_required
def post_query():
    return postQuery(request.get_json())

@bp.route('/queryByCategory', methods=['GET'])
@resp_wrapper
@json_required
def post_query_by_category():
    return postQueryByCategory(request.get_json())

@bp.route('/queryByTag', methods=['GET'])
@resp_wrapper
@json_required
def post_query_by_tag():
    return postQueryByTag(request.get_json())

@bp.route('/queryArchives', methods=['GET'])
@resp_wrapper
@json_required
def post_query_archives():
    return postQueryByTag(request.get_json())

@bp.route('/queryArchivesByCategory', methods=['GET'])
@resp_wrapper
@json_required
def post_query_archives_by_category():
    return postQueryByTag(request.get_json())

@bp.route('/queryArchivesByTag', methods=['GET'])
@resp_wrapper
@json_required
def post_query_archives_by_tag():
    return postQueryByTag(request.get_json())

@bp.route('/queryDetail', methods=['GET'])
@resp_wrapper
@json_required
def post_query_detail():
    return postQueryDetail(request.get_json())