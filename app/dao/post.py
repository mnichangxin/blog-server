from flask import jsonify
from datetime import datetime
from ..libs.error import APIException
from ..model import db
from ..model import PostModel, CategoryModel, TagModel


class Post:
    def insertPost(self):
        post = PostModel(title='title1', content='123456', first_date=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        return ''

    def getPosts(self, offset=0, limit=10):
        if not (limit and limit <= 50):
            raise APIException(u'limit must between 0 and 50', 400)
        return PostModel.query.all()
