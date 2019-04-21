from flask import jsonify
from .. import api

@api.route('/admin/login', methods=['POST'])
def login():
    return 'admin login.'

@api.route('/admin/logout', methods=['POST'])
def logout():
    return 'admin logout.'

@api.route('/admin/publish', methods=['POST'])
def publish():
    return 'publish'
