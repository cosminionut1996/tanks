import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'development',
        'host': 'localhost',
        'port': 27017
    }
    REDIS_URL = "redis://localhost:6379/1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'testing',
        'host': 'localhost',
        'port': 27017
    }
    REDIS_URL = "redis://localhost:6379/2"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'production',
        'host': 'localhost',
        'port': 27017
    }
    REDIS_URL = "redis://localhost:6379/0"

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
