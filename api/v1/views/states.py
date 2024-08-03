#!/usr/bin/python3
"""default rest api actions for state objects.
    """
from flask import abort, request
from api.v1.views import app_views
from models import storage
from models.state import State
from api.v1.views.object_boilerplate import (get_all_of_class,
                                                get_specific_instance,
                                                delete_instance,
                                                post_instance,
                                                update_instance)


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def get_all_states():
    """gets all available states and returns them as a dict"""
    return get_all_of_class(State)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_specific_state(state_id):
    """gets a specific state according to its id, or 404 on fail"""
    return get_specific_instance(State, state_id)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['DELETE'])
def delete_state(state_id):
    """deletes a state according to its id, or 404 on fail"""
    return delete_instance(State, state_id)


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def post_state():
    """adds a new state, requires a name in a json"""
    try:
        data = request.get_json()
    except:
        abort(400, description="Not a JSON")

    if data.get('name', None) is None:
        abort(400, description="Missing name")

    return post_instance(State, **data)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def update_state(state_id):
    """updates a new state given key value pairs"""
    return update_instance(State, state_id)
