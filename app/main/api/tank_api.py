import json
from http import HTTPStatus

from flask import request
from flask_restx import Resource

from ..core.tank_core import TankCore
from ..util.dto import TankDto as Dto

api = Dto.api
tank_model = Dto.tank_model

@api.route('')
class TankList(Resource):

    @api.doc('Create a tank and save it into the database')
    @api.expect(tank_model)
    @api.marshal_with(tank_model)
    def post(self):
        tank_object, status = TankCore.create(
            request.json.get('health'),
            request.json.get('damage')
        )
        return json.loads(tank_object), status

    @api.doc('Return all tank objects and filter them accordingly')
    # @api.marshal_list_with(tank_model)
    def get(self):
        return TankCore.get_all()


@api.route('/<object_id>')
class Tank(Resource):

    @api.doc('Retrieve a tank from the database')
    @api.expect(tank_model)
    @api.marshal_with(tank_model)
    def get(self, object_id):
        tank_object, status = TankCore.get(object_id)
        return json.loads(tank_object), status

    @api.doc('Delete a tank')
    def delete(self, object_id):
        return TankCore.delete(object_id)
