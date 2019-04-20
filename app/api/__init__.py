from flask import Blueprint, jsonify
from datetime import datetime
# from ..db.models import db, Article, Category, Tag

api = Blueprint('api', __name__)

@api.route('/')
def root():
    return 'Api connection...'

# @api.route('/view')
# def view():
#     Article.query()
#     return jsonify({
#         'name': 1
#     })