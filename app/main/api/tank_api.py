from http import HTTPStatus

# from flask import request
from flask_restx import Resource
# from werkzeug.exceptions import BadRequest

# from ..model.user import User
# from ..service.auth_helper import get_logged_in_user
# from ..service.group_service import (create_group, delete_group, get_a_group,
#                                      get_groups, update_group)
# from ..util.decorator import token_required
from ..util.dto import TankDto as Dto

api = Dto.api
tank_model = Dto.tank_model

@api.route('')
class TankList(Resource):

    @api.doc('Create a tank and save it into the database')
    @api.marshal_with(tank_model)
    def post(self):
        pass


@api.route('/<uuid_tank>')
class Tank(Resource):

    @api.doc('Retrieve a tank from the database')
    @api.expect(tank_model)
    @api.marshal_with(tank_model)
    def get(self, uuid_tank):
        pass

    @api.doc('Delete a tank')
    def delete(self, uuid_tank):
        pass
