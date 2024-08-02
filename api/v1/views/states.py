#!/usr/bin/python3
"""default rest api actions for state objects.
    """
from flask import abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def get_all_states():
    """gets all available states and returns them as a dict"""
    ret = []
    all_states = storage.all(State)
    for _, state in all_states.items():
        ret.append(state.to_dict())
    return ret


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_specific_state(state_id):
    """gets all available states and returns them as a dict"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.to_dict()


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['DELETE'])
def delete_state(state_id):
    """gets all available states and returns them as a dict"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return {}


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def post_state():
    """gets all available states and returns them as a dict"""
    try:
        data = request.get_json()
    except:
        abort(400, description="Not a JSON")
    if data.get('name', None) is None:
        abort(400, description="Missing name")
    newstate = State(name=data['name'])
    storage.new(newstate)
    storage.save()
    return newstate.to_dict(), 201
