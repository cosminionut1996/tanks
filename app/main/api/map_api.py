import json
from http import HTTPStatus

from flask import request
from flask_restx import Resource

from ..core.map_core import MapCore
from ..util.dto import MapDto as Dto

api = Dto.api
map_model = Dto.map_model

@api.route('')
class MapList(Resource):

    @api.doc('Create a map and save it into the database')
    @api.expect(map_model, validate=True)
    @api.marshal_with(map_model)
    def post(self):
        map_object, status = MapCore.create(
            request.json.get('height'),
            request.json.get('width'),
            [],
            [],
            []
        )
        return json.loads(map_object), status

    # @api.doc('Filter and return a list of maps')
    # def get(self):
    #     pass

@api.route('/<object_id>')
class Map(Resource):

    @api.doc('Retrieve a map from the database')
    @api.response(HTTPStatus.FOUND, 'Did manage to find the requested map')
    @api.response(HTTPStatus.NOT_FOUND, 'Did not find a map corresponding to the object id')
    @api.marshal_with(map_model)
    def get(self, object_id):
        map_object, status = MapCore.get(object_id)
        return json.loads(map_object), status

    @api.doc('Delete the map object with the specified id')
    @api.response(HTTPStatus.NOT_FOUND, 'Did not find a map corresponding to the object id')
    @api.response(HTTPStatus.OK, 'Did manage to find and delete the requested map')
    def delete(self, object_id):
        _, status = MapCore.delete(object_id)
        return _, status
