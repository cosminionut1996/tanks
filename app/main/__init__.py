from flask import Flask
from flask_mongoengine import MongoEngine
from flask_redis import FlaskRedis

from .config import config_by_name

mongo = MongoEngine()
redis = FlaskRedis()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    mongo.init_app(app)
    redis.init_app(app)
    return app
