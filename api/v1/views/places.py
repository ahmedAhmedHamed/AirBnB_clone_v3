#!/usr/bin/python3
"""default rest api actions for place objects.
    """
from api.v1.views import app_views
from models.place import Place
from api.v1.views.object_boilerplate import (instance_list_to_dict_list,
                                             get_specific_instance,
                                             delete_instance,
                                             post_instance,
                                             update_instance)
from models import storage
from models.city import City
from flask import abort, request

from models.user import User


@app_views.route(
    '/cities/<city_id>/places', strict_slashes=False, methods=['GET'])
def get_all_related_places(city_id):
    """gets all available places and returns them as a dict"""
    city: City = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = city.places
    return instance_list_to_dict_list(places)


@app_views.route(
    '/places/<place_id>', strict_slashes=False, methods=['GET'])
def get_specific_place(place_id):
    """gets a specific place according to its id, or 404 on fail"""
    return get_specific_instance(Place, place_id)


@app_views.route(
    '/places/<place_id>', strict_slashes=False, methods=['DELETE'])
def delete_place(place_id):
    """deletes an place according to its id, or 404 on fail"""
    return delete_instance(Place, place_id)


@app_views.route(
    '/cities/<city_id>/places', strict_slashes=False, methods=['POST'])
def post_place(city_id):
    """adds a new place, requires a name in a json"""
    try:
        data = request.get_json()
    except:
        abort(400, description="Not a JSON")
    city: City = storage.get(City, city_id)
    if city is None:
        abort(404)
    user: User = storage.get(User, data.get('user_id'))
    if user is None:
        abort(400, description="Missing user_id")
    if data.get('name') is None:
        abort(400, description="Missing name")
    return post_instance(Place, **data)


@app_views.route(
    '/places/<place_id>', strict_slashes=False, methods=['PUT'])
def update_place(place_id):
    """updates a new place given key value pairs"""
    ignored_keys = ["id", "user_id", "city_id", "created_at", "updated_at"]
    return update_instance(Place, place_id, ignored_keys)
