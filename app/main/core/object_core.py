import json
from abc import ABC
from http import HTTPStatus

from bson.objectid import ObjectId


class Core(ABC):

    MODEL = None

    @classmethod
    def create(cls, **kwargs):
        new_object = cls.MODEL(
            **kwargs
        )
        new_object.save()
        return new_object.to_json(), HTTPStatus.CREATED

    @classmethod
    def get(cls, object_id, _whole_obj=False):
        try:
            found = cls.MODEL.objects.get(id=ObjectId(object_id))
        except cls.MODEL.DoesNotExist:
            return json.dumps(dict(
                error='Could not find the object of type {} with the requested object id' \
                       .format(type(cls.MODEL))
            )), HTTPStatus.NOT_FOUND
        else:
            return found if _whole_obj else found.to_json(), HTTPStatus.FOUND

    @classmethod
    def delete(cls, object_id):
        found, status = cls.get(object_id, _whole_obj=True)
        if status == HTTPStatus.FOUND:
            found.delete()
            return None, HTTPStatus.OK

        return None, HTTPStatus.NOT_FOUND
