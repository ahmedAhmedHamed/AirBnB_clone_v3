#!/usr/bin/python3
"""default rest api actions for state objects.
    """
from flask import abort
from api.v1.views import app_views
from models.engine.db_storage import classes
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def get_all_states():
    """gets all available states and returns them as a dict"""
    ret = []
    all_states = storage.all(State)
    for _, state in all_states.items():
        ret.append(state.to_dict())
    return ret


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_specific_state(state_id):
    """gets all available states and returns them as a dict"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.to_dict()

