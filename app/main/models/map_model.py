from .. import mongo

class Map(mongo.Document):

    # _id = mongo.ObjectIdField()
    height = mongo.IntField(required=True, min_value=50)
    width = mongo.IntField(required=True, min_value=50)

    # obstacles = mongo.ListField(
    #     mongo.Tuple
    # )
