import json
from http import HTTPStatus

from flask import request
from flask_restx import Resource

from ..core.battle_core import BattleCore
from ..util.dto import BattleDto as Dto

api = Dto.api
battle_model = Dto.battle_model


@api.route('')
class BattleList(Resource):

    @api.doc(
        'Create a battle between two tanks. ' \
        'The result will be used for querying the result of the battle. ' \
        'The battle is ran asynchronously.')
    @api.expect(battle_model)
    @api.marshal_with(battle_model)
    def post(self):
        battle_object, status = BattleCore.create(
            request.json.get('tank1_id'),
            request.json.get('tank2_id'),
            request.json.get('map_id')
        )
        return json.loads(battle_object), status

    @api.doc('Return all battle objects and filter them accordingly')
    @api.marshal_with(battle_model)
    def get(self):
        return BattleCore.get_all()


@api.route('/<object_id>')
class Battle(Resource):

    @api.doc('Retrieve a battle from the database.')
    @api.response(HTTPStatus.FOUND, 'Did manage to find the requested battle')
    @api.response(HTTPStatus.NOT_FOUND, 'Did not find a battle corresponding to the object id')
    @api.marshal_with(battle_model)
    def get(self, object_id):
        battle_object, status = BattleCore.get(object_id)
        return json.loads(battle_object), status
    
    @api.doc('Delete the battle object with the specified id')
    @api.response(HTTPStatus.NOT_FOUND, 'Did not find a battle corresponding to the object id')
    @api.response(HTTPStatus.OK, 'Did manage to find and delete the requested battle')
    def delete(self, object_id):
        return BattleCore.delete(object_id)
