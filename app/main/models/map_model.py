from .. import mongo
from .embedded import Coordinate


class Map(mongo.Document):

    # _id = mongo.ObjectIdField()
    height = mongo.IntField(required=True, min_value=50)
    width = mongo.IntField(required=True, min_value=50)

    tank1_start = mongo.EmbeddedDocumentField(Coordinate)
    tank2_start = mongo.EmbeddedDocumentField(Coordinate)

    obstacles = mongo.EmbeddedDocumentListField(Coordinate)
