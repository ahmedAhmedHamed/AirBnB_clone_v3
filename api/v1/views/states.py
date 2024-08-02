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
    """gets a specific state according to its id, or 404 on fail"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.to_dict()


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['DELETE'])
def delete_state(state_id):
    """deletes a state according to its id, or 404 on fail"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return {}


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def post_state():
    """adds a new state, requires a name in a json"""
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


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def update_state(state_id):
    """updates a new state given key value pairs"""
    try:
        data = request.get_json()
    except:
        abort(400, description="Not a JSON")
    state = storage.get(State, state_id)
    if state is None:
        return abort(404)
    for key, value in data.items():
        if key == "id" or key == "created_at" or key == "updated_at":
            continue
        setattr(state, key, value)
    storage.save()
    return state.to_dict(), 200
