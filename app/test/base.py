
from flask_testing import TestCase

from app.main import mongo
from app.main import redis
from app.main.config import TestingConfig
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object(TestingConfig)
        self.api_ver = '/api/v1'
        return app

    def setUp(self):
        mongo.connection.drop_database(
            TestingConfig.MONGODB_SETTINGS.get('db')
        )

    # def tearDown(self):
    #     mongo.connection.drop_database(
    #         TestingConfig.MONGODB_SETTINGS.get('db')
    #     )
