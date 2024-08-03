#!/usr/bin/python3
"""default rest api actions for amenity objects.
    """
from flask import request, abort

from api.v1.views import app_views
from models.amenity import Amenity
from api.v1.views.object_boilerplate import (get_all_of_class,
                                                get_specific_instance,
                                                delete_instance,
                                                post_instance,
                                                update_instance)


@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
def get_all_amenities():
    """gets all available amenities and returns them as a dict"""
    return get_all_of_class(Amenity)


@app_views.route(
    '/amenities/<amenity_id>', strict_slashes=False, methods=['GET'])
def get_specific_amenity(amenity_id):
    """gets a specific amenity according to its id, or 404 on fail"""
    return get_specific_instance(Amenity, amenity_id)


@app_views.route(
    '/amenities/<amenity_id>', strict_slashes=False, methods=['DELETE'])
def delete_amenity(amenity_id):
    """deletes an amenity according to its id, or 404 on fail"""
    return delete_instance(Amenity, amenity_id)


@app_views.route('/amenities', strict_slashes=False, methods=['POST'])
def post_amenity():
    """adds a new amenity, requires a name in a json"""
    try:
        data = request.get_json()
    except:
        abort(400, description="Not a JSON")

    if data.get('name', None) is None:
        abort(400, description="Missing name")

    return post_instance(Amenity, **data)


@app_views.route(
    '/amenities/<amenity_id>', strict_slashes=False, methods=['PUT'])
def update_amenity(amenity_id):
    """updates a new amenity given key value pairs"""
    ignored_keys = ["id", "created_at", "updated_at"]
    return update_instance(Amenity, amenity_id, ignored_keys)
