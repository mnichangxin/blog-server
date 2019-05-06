from flask import jsonify
from datetime import datetime
from ..libs.error import APIException
from . import db
from .models import PostModel, CategoryModel, TagModel


class Post:    
    def insertPost(self):
        try:
            post = PostModel(title='title1', content='123456', first_date=datetime.utcnow())
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify({
                'status': 0,
                'msg': 'err'
            })
        else:
            return jsonify({
                'status': 1,
                'msg': '成功'
            })

    def getPosts(self, offset=0, limit=10):
        if not (limit and limit <= 50):
            raise APIException(u'limit must between 0 and 50', 400)
        return PostModel.query.all()
