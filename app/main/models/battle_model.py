from .. import mongo

class BattleModel(mongo.Document):

    tank1_id = mongo.ObjectIdField(required=True)
    tank2_id = mongo.ObjectIdField(required=True)
    map_id = mongo.ObjectIdField(required=True)

    moves = mongo.ListField()
