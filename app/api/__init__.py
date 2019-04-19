from flask import Blueprint, jsonify
from datetime import datetime
from ..db.models import db, Article, Category, Tag

api = Blueprint('api', __name__)

@api.route('/')
def root():
    return 'Api connection...'

@api.route('/view')
def view():
    Article.query()
    return jsonify({
        'name': 1
    })
    
@api.route('submit', methods=['POST'])
def submit():
    category = Category(category_name='program')
    tag = Tag('tag1')
    article = Article(title='title', content='content', category=category, tag=tag)
    db.session.add(article)
    db.session.commit()