from flask import Blueprint, jsonify

blog = Blueprint('blog', __name__)

@blog.route('/')
@blog.route('/index')
def get_index():
    return jsonify('Blog index')
