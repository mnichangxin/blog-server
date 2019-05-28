from datetime import datetime

from flask import Blueprint, jsonify, request
from ...libs.decorators import resp_wrapper
from ...dao import Post

admin = Blueprint('admin', __name__)

@admin.route('/publish', methods=['POST'])
@resp_wrapper
def publish():
    data = request.data
    return Post().insertPost()