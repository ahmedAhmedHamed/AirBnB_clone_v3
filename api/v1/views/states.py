#!/usr/bin/python3
"""default rest api actions for state objects.
    """
from flask import jsonify
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

