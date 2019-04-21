from flask import jsonify
from .. import api

@api.route('/blog')
@api.route('/blog/index')
def get_index():
    return jsonify('Blog index')
