from http import HTTPStatus

from ..models.tank_model import TankModel
from .object_core import Core


class TankCore(Core):

    MODEL = TankModel

    @classmethod
    def create(cls,
        health,
        damage,
    ):
        return super().create(
            health=health,
            damage=damage
        )
