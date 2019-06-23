from flask import Blueprint, jsonify
from ...dao import Post

blog = Blueprint('blog', __name__)

@blog.route('/')
@blog.route('/index')
def get_index():
    print(Post().getPosts(0, 100))
    return jsonify('Blog index')
