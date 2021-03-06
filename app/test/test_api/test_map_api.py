import json
from http import HTTPStatus

from app.test.base import BaseTestCase


class TestMapApi(BaseTestCase):

    def test_create_get_delete(self):

        with self.client:
            response = self.client.post(
                self.api_ver + '/maps',
                data=json.dumps({
                    'height': 50,
                    'width': 50,
                    'tank1_start': {
                        'x': 1,
                        'y': 2
                    },
                    'tank2_start': {
                        'x': 3,
                        'y': 4
                    }
                }),
                content_type='application/json'
            )
            self.assertEquals(response.status_code, HTTPStatus.CREATED)
            self.assertEquals(response.json.get('height'), 50)
            self.assertEquals(response.json.get('tank1_start').get('x'), 1)

            map_id = response.json.get('_id')
            response = self.client.get(
                self.api_ver + '/maps/{}'.format(map_id)
            )
            self.assertEquals(response.status_code, HTTPStatus.FOUND)
            self.assertEquals(response.json.get('width'), 50)
            self.assertEquals(response.json.get('tank2_start').get('y'), 4)

            response = self.client.delete(
                self.api_ver + '/maps/{}'.format(map_id)
            )

            response = self.client.get(
                self.api_ver + '/maps/{}'.format(map_id)
            )
            self.assertEquals(response.status_code, HTTPStatus.NOT_FOUND)
 