from flask import Blueprint, request
from server.utils.common.redprint import Redprint
from server.utils.decorators.res_wrapper import resp_wrapper
from server.service.common import post_publish, post_query, post_delete, post_update

post = Redprint('post')

@post.route('/publish', methods=['POST'])
@resp_wrapper
def post_publish():
    return post_publish(request.get_json())

@post.route('/query', methods=['GET'])
@resp_wrapper
def post_query():
    return post_query(request.get_json())

@post.route('/delete', methods=['POST'])
@resp_wrapper
def post_delete():
    return post_delete(request.get_json())

@post.route('/update', methods=['POST'])
@resp_wrapper
def post_update():
    return post_update(request.get_json())