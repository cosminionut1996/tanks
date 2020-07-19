import json
from http import HTTPStatus

from app.test.base import BaseTestCase


class TestTankApi(BaseTestCase):

    def test_create_multi_get_all(self):

        values = list(range(10, 20))

        with self.client:
            for damage, health in zip(values, values):
                response = self.client.post(
                    self.api_ver + '/tanks',
                    data=json.dumps({
                        'damage': damage,
                        'health': health
                    }),
                    content_type='application/json'
                )
                self.assertEquals(response.status_code, HTTPStatus.CREATED)
                self.assertEquals(response.json.get('damage'), damage)
                self.assertEquals(response.json.get('health'), health)

            response = self.client.get(self.api_ver + '/tanks')
            self.assertEquals(response.status_code, HTTPStatus.FOUND)
            self.assertEquals(len(response.json), len(values))
