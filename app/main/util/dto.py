from flask_restx import Model, Namespace, fields, reqparse


class ObjectIDField(fields.Raw):
    def format(self, value):
        return value.get('$oid')


class TankDto:
    api = Namespace('tanks', description='Tank object related operations')
    tank_model = api.model('Tank', {
        '_id': ObjectIDField(description='Tank ID'),
        'health': fields.Integer(required=True, description='Tank health'),
        'damage': fields.Integer(required=True, description='Tank damage')
    })

class MapDto:
    api =  Namespace('maps', description='Map object related operations')

    coordinate_model = api.model('Coordinate', {
        'x': fields.Integer(required=True, description='x coordinate'),
        'y': fields.Integer(required=True, description='y coordinate')
    })

    map_model = api.model('Map', {
        '_id': ObjectIDField(description='Map ID'),
        'height': fields.Integer(required=True, description='Map height'),
        'width': fields.Integer(required=True, description='Map width'),
        'tank1_start': fields.Nested(coordinate_model, required=True, description='Starting position for the first tank'),
        'tank2_start': fields.Nested(coordinate_model, required=True, description='Starting position for the second tank')
        # 'obstacles': fields.List(
        #     fields.List(
        #         fields.Integer(),
        #         # min_items=2,
        #         # max_items=2,
        #         description='An obstacle is a list of integers that represent X and Y coordinates on the map'
        #     ),
        #     description='The list of obstacles'
        # ),
    })

class BattleDto:
    api = Namespace('battle', description='Battle object related operations')
    battle_model = api.model('Battle', {
        '_id': ObjectIDField(description='Battle ID'),
        'tank1_id': ObjectIDField(description='Object ID of the first tank'),
        'tank2_id': ObjectIDField(description='Object ID of the second tank'),
        'map_id': ObjectIDField(description='Object ID of the map'),
        # 'moves': fields.List(description='List of moves')
    })
