class BaseConfig:
    '''Base config'''
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = '''mysql+mysqlconnector://root:12345678@localhost:3306
                                                    /blog?charset=utf8'''
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
