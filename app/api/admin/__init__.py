from datetime import datetime

from flask import Blueprint, jsonify, request
from ...libs.decorators import resp_wrapper
from ...db import Post

admin = Blueprint('admin', __name__)

@admin.route('')
@admin.route('/')
def get_admin_api():
    return jsonify({
        'api': 'admin'
    })

@admin.route('/login', methods=['POST'])
def login():
    return 'admin login.'

@admin.route('/logout', methods=['POST'])
def logout():
    return 'admin logout.'

@admin.route('/publish', methods=['POST'])
@resp_wrapper
def publish():
    data = request.data
    return Post().insertPost()