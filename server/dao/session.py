from server.model import db
from server.model.tb_session import SessionModel

class Session:
    @staticmethod
    def insert(**kwargs):
        session = SessionModel(**kwargs)
        db.session.add(session)
        db.session.flush()
        return session
    @staticmethod
    def queryBySessionId(session_id):
        return SessionModel.query.filter_by(session_id=session_id).first()