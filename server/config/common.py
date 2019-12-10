'''
    Notice: The database config is confidential information, so not open source code. You can create owner db config If you need. 
'''
from .db_secure import config as db_config

class BaseConfig:
    '''Base config'''
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = '''mysql+mysqlconnector://{username}:{password}@{host}/{database}?charset={charset}''' \
                                .format(host=db_config['HOST'], port=db_config['PORT'], \
                                username=db_config['USERNAME'], password=db_config['PASSWORD'], \
                                database=db_config['DATABASE'], charset=db_config['CHARSET'])
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    '''Development config'''
    DEBUG = True


class TestingConfig(BaseConfig):
    '''Testing config'''
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}