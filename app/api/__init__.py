from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('')
@api.route('/')
def get_api():
    return jsonify({
        'version': '1.0'
    })

