#!/usr/bin/python3
"""default rest api actions for city objects.
    """
from flask import abort, request, jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', strict_slashes=False)
def get_all_cities(state_id):
    """gets all cities for a given state, or 404 on fail"""
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', strict_slashes=False)
def get_city(city_id):
    """gets all cities for a given state, or 404 on fail"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)
    
@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """delete city"""
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)
    
@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """create a new city"""
    if request.content_type != 'application/json':
        return abort(404, 'NOT a JSON')
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    if not request.get_json():
        return abort(400, 'NOT a JSON')
    data = request.get_json()
    if 'name' not in data:
        return abort(400, 'Missing name')
    data['state_id'] = state_id
    
    city = City(**data)
    city.save()
    return jsonify(city.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """update city"""
    if request.content_type != 'application/json':
        return abort(404, 'NOT a JSON')
    city = storage.get(City, city_id)
    if city:
        if not request.get_json():
            return abort(400, 'NOT a JSON')
        data = request.get_json()
        ignore_key = ['id', 'state_id', 'created_at', 'updated_at']

        for key, value in data.items():
            if key not in ignore_key:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
    else:
        return abort(404)
