from datetime import datetime

from flask import Blueprint, jsonify, request, current_app
from ...libs.decorators import resp_wrapper
from ...dao import Post

admin = Blueprint('admin', __name__)

@admin.route('/publish', methods=['POST'])
@resp_wrapper
def publish():
    params = request.get_json()
    return Post().insertPost(params)