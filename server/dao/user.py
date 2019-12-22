from server.model import db
from server.model.tb_user import UserModel

class User:
    @staticmethod
    def insert(**kwargs):
        user = UserModel(**kwargs)
        db.session.add(user)
        db.session.flush()
        return user
    @staticmethod
    def queryByUserName(username):
        return UserModel.query.filter_by(username=username).first()