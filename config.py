from os import getenv


class BaseConfig(object):
    ERROR_INCLUDE_MESSAGE = False
    SESSION_COOKIE_SECURE = True

    DEBUG = False
    TESTING = False

    # https://flask-caching.readthedocs.io/en/latest/#configuring-flask-caching
    CACHE_TYPE = 'filesystem'
    CACHE_KEY_PREFIX = 'auche_'
    CACHE_DIR = 'tmp/cache'
    CACHE_THRESHOLD = 0
    CACHE_DEFAULT_TIMEOUT = 0

    # DB 接続
    DATABASE_NAME = getenv('APP_DATABASE_NAME', 'app')
    DATABASE_HOST = getenv('APP_DATABASE_HOST')
    DATABASE_USER = getenv('APP_DATABASE_USER', 'app')
    DATABASE_PASSWORD = getenv('AUCHE_DATABASE_PASSWORD')
    SQLALCHEMY_DATABASE_URI = None

    # 発行された SQL をログに出力するかどうか
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init_subclass__(cls, **kwargs):
        cls.SQLALCHEMY_DATABASE_URI = (
            'mysql+mysqlconnector://' +
            f'{cls.DATABASE_USER}:{cls.DATABASE_PASSWORD}@{cls.DATABASE_HOST}' +
            f'/{cls.DATABASE_NAME}?charset=utf8mb4'
        )


class ProductionConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_ECHO = True


class TestConfig(BaseConfig):
    TESTING = True

    DATABASE_HOST = getenv('APP_DATABASE_HOST', '127.0.0.1')
    DATABASE_USER = getenv('APP_DATABASE_USER', 'app')
    DATABASE_PASSWORD = getenv('APP_DATABASE_PASSWORD', 'app')
    DATABASE_NAME = 'app_test'
