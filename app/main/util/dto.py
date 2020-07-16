from flask_restx import Model, Namespace, fields, reqparse


class ObjectIDField(fields.Raw):
    def format(self, value):
        return value.get('$oid')


class TankDto:
    api = Namespace('tanks', description='Tank object related operations')
    tank_model = api.model('Tank', {

    })

class MapDto:
    api =  Namespace('maps', description='Map object related operations')
    map_model = api.model('Map', {
        '_id': ObjectIDField(description='Object id'),
        'height': fields.Integer(required=True, description='Map height'),
        'width': fields.Integer(required=True, description='Map width'),
        # 'obstacles': fields.List(
        #     fields.List(
        #         fields.Integer(),
        #         # min_items=2,
        #         # max_items=2,
        #         description='An obstacle is a list of integers that represent X and Y coordinates on the map'
        #     ),
        #     description='The list of obstacles'
        # ),
        # 'start_1': fields.List(
        #     fields.Integer(),
        #     required=True,
        #     # min_items=2,
        #     # max_items=2,
        #     description='The X and Y coordinates of the first starting position'
        # ),
        # 'start_2': fields.List(
        #     fields.Integer(),
        #     required=True,
        #     # min_items=2,
        #     # max_items=2,
        #     description='The X and Y coordinates of the second starting position'
        # ),
    })

class BattleDto:
    api = Namespace('battle', description='Battle object related operations')
    battle_model = api.model('Battle', {

    })
