from flask import jsonify
from datetime import datetime
from ..utils.exception.exception import APIException
from ..model.common import db
from ..model.post import PostModel


class Post:
    def insert(self, *arg, **kwargs):
        post = PostModel(arg)
        db.session.add(post)
        db.session.commit()
        return ''
    def get(self, offset=0, limit=10):
        if not (limit and limit <= 50):
            raise APIException(u'limit must between 0 and 50', 400)
        return PostModel.query.all()
