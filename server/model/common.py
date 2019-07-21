from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={
    'autocommit': True
})

'''
    Convert Model object to dict
'''
def to_dict(self):
    return { column.name: getattr(self, column.name, None) for column in self.__table__.columns }

db.Model.to_dict = to_dict