from ... import mongo


class Coordinate(mongo.EmbeddedDocument):

    x = mongo.IntField(required=True)
    y = mongo.IntField(required=True)
