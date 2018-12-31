import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    '''
    Base config`
    '''
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    '''
    Development config
    '''
    DEBUG = True


class TestingConfig(BaseConfig):
    '''
    Testing config
    '''
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
