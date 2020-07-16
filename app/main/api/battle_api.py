from http import HTTPStatus

# from flask import request
from flask_restx import Resource
# from werkzeug.exceptions import BadRequest

# from ..model.user import User
# from ..service.auth_helper import get_logged_in_user
# from ..service.group_service import (create_group, delete_group, get_a_group,
#                                      get_groups, update_group)
# from ..util.decorator import token_required
from ..util.dto import BattleDto as Dto

api = Dto.api


@api.route('')
class BattleList(Resource):

    @api.doc(
        'Create a battle between two tanks. ' \
        'The result will be used for querying the result of the battle. ' \
        'The battle is ran asynchronously.')
    def post(self):
        pass

    @api.doc('Filter and export a list of battles.')
    def get(self):
        pass

@api.route('/<uuid_battle>')
class Battle(Resource):

    @api.doc('Retrieve a battle from the database.')
    def get(self, uuid_battle):
        pass
