import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = 'dev'
    # DATABASE = os.path.join(basedir, 'instance', 'flaskr.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False

config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
