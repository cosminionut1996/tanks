from http import HTTPStatus

from ..models.battle_model import BattleModel
from .object_core import Core


class BattleCore(Core):

    MODEL = BattleModel

    @classmethod
    def create(cls,
        tank1_id,
        tank2_id,
        map_id
    ):
        return super().create(
            tank1_id=tank1_id,
            tank2_id=tank2_id,
            map_id=map_id
        )
