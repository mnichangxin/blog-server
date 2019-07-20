from .common import db

class Base(db.Model):
    def to_dict(self):
        return { column.name: getattr(self, column.name, None) for column in self.__table__.columns }
    
    def __repr__(self):
        return '<Base>'