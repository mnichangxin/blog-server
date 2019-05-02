from datetime import datetime

from flask import Blueprint, jsonify
# from ...db.models import db, Post, Category, Tag
from ...db.models.post import PostModel
from ...db.models.category import CategoryModel
from ...db.models.tag import TagModel

admin = Blueprint('admin', __name__)

@admin.route('/login', methods=['POST'])
def login():
    return 'admin login.'

@admin.route('/logout', methods=['POST'])
def logout():
    return 'admin logout.'

@admin.route('/publish', methods=['POST'])
def publish():
    category = Category(category_name='git')
    tag = Tag(tag_name='javascript')
    post = Post(title='title1', content='123456', date=datetime.utcnow())
    db.session.add(category)
    db.session.add(tag)
    db.session.add(post)
    category.posts.append(post)
    tag.posts.append(post)
    db.session.commit()
    return 'publish'

@admin.route('/get')
def get():
    # res = []
    # posts = Post.query.all()
    # for i range(len(posts)):
    #     res
    print(Post.query.all()[0].tags[0].tag_name)
    return ''