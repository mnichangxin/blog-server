from flask import jsonify
from datetime import datetime
from ..utils.exception.exception import APIException
from ..model.common import db
from ..model.post import PostModel


class Post:
    def insertPost(self, *arg, **kwargs):
        content = kwargs.get('cotent')
        first_date = kwargs.get('first_date')
        if content is None or first_date is None:
            raise APIException(u'参数错误', 400)
        post = PostModel(arg)
        db.session.add(post)
        db.session.commit()
        return ''

    def getPosts(self, offset=0, limit=10):
        if not (limit and limit <= 50):
            raise APIException(u'limit must between 0 and 50', 400)
        return PostModel.query.all()
