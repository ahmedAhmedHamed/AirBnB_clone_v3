#!/usr/bin/python3
"""This is the main entry point for the Flask application.
    """
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ Returns the status of the application """
    return jsonify({"status": "OK"})
