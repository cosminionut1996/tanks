from http import HTTPStatus

from ..models.map_model import Map
from .object_core import Core


class MapCore(Core):

    MODEL = Map

    @classmethod
    def create(cls,
        width,
        height,
        tank1_start,
        tank2_start,
        obstacles
    ):
        return super().create(
            width=width,
            height=height,
            tank1_start=tank1_start,
            tank2_start=tank2_start
            # obstacles=obstacles
        )
