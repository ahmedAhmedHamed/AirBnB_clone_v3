#!/usr/bin/python3
"""This is the main entry point for the Flask application.
    """
from flask import jsonify
from api.v1.views import app_views
from models.engine.db_storage import classes
from models import storage


@app_views.route('/status')
def status():
    """ Returns the status of the application """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def all_object_count():
    ret = {}
    for class_name, class_type in classes.items():
        count = storage.count(class_type)
        ret[class_name] = count
    return jsonify(ret)
