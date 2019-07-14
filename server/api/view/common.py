from flask import Blueprint, jsonify

view = Blueprint('view', __name__)

@view.route('/')
@view.route('/index')
def get_index():
    return jsonify('view api')