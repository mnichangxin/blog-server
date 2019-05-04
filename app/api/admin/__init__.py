from datetime import datetime

from flask import Blueprint, jsonify
from ...db import Post

admin = Blueprint('admin', __name__)

@admin.route('/login', methods=['POST'])
def login():
    return 'admin login.'

@admin.route('/logout', methods=['POST'])
def logout():
    return 'admin logout.'

@admin.route('/publish', methods=['POST'])
def publish():
    return 'publish'