from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, \
                                                        ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost:3306/blog?charset=utf8mb4')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.username)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
