#!/usr/bin/python3
"""default rest api actions for state objects.
    """
from flask import abort, request
from models import storage


def get_all_of_class(cls):
    """gets all available states and returns them as a dict"""
    ret = []
    all_of_class = storage.all(cls)
    for _, class_instance in all_of_class.items():
        ret.append(class_instance.to_dict())
    return ret


def get_specific_instance(cls, instance_id):
    """gets a specific state according to its id, or 404 on fail"""
    instance = storage.get(cls, instance_id)
    if instance is None:
        abort(404)
    return instance.to_dict()


def delete_instance(cls, instance_id):
    """deletes a state according to its id, or 404 on fail"""
    instance = storage.get(cls, instance_id)
    if instance is None:
        abort(404)
    storage.delete(instance)
    storage.save()
    return {}


def post_instance(cls):
    """adds a new state, requires a name in a json"""
    try:
        data = request.get_json()
    except:
        abort(400, description="Not a JSON")
    if data.get('name', None) is None:
        abort(400, description="Missing name")
    new_object = cls(name=data['name'])
    storage.new(new_object)
    storage.save()
    return new_object.to_dict(), 201


def update_instance(cls, object_id):
    """updates a new state given key value pairs"""
    try:
        data = request.get_json()
    except:
        abort(400, description="Not a JSON")
    instance = storage.get(cls, object_id)
    if instance is None:
        return abort(404)
    for key, value in data.items():
        if key == "id" or key == "created_at" or key == "updated_at":
            continue
        setattr(instance, key, value)
    storage.save()
    return instance.to_dict(), 200
