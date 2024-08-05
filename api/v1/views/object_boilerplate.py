#!/usr/bin/python3
"""default rest api actions for state objects.
    """
from flask import abort, request
from models import storage


def instance_list_to_dict_list(instance_list):
    """ Return a list of instances
    """
    ret = []
    for _, class_instance in instance_list.items():
        ret.append(class_instance.to_dict())
    return ret


def get_all_of_class(cls):
    """gets all available states and returns them as a dict"""
    all_of_class = storage.all(cls)
    return instance_list_to_dict_list(all_of_class)


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


def post_instance(cls, **kwargs):
    """adds a new state, requires a name in a json"""
    new_object = cls(**kwargs)
    storage.new(new_object)
    storage.save()
    return new_object.to_dict(), 201


def update_instance(cls, object_id, ignore_list=None):
    """updates a new state given key value pairs"""
    if ignore_list is None:
        ignore_list = []
    try:
        data = request.get_json()
    except Exception:
        abort(400, description="Not a JSON")
    instance = storage.get(cls, object_id)
    if instance is None:
        return abort(404)
    for key, value in data.items():
        if key in ignore_list:
            continue
        setattr(instance, key, value)
    storage.save()
    return instance.to_dict(), 200
