from flask_restx import Api
from flask import Blueprint

from .main.api.tank_api import api as tank_ns
from .main.api.map_api import api as map_ns
from .main.api.battle_api import api as battle_ns


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(
    blueprint,
    title='Tanks',
    version='1.0',
    description='Tank battle simulator',
    doc='/docs'
)

api.add_namespace(tank_ns, path='/tanks')
api.add_namespace(map_ns, path='/maps')
api.add_namespace(battle_ns, path='/battle')
