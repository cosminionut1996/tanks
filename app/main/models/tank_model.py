from .. import mongo

class TankModel(mongo.Document):

    health = mongo.IntField(required=True)
    damage = mongo.IntField(required=True)
