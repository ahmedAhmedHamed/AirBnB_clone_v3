#!/usr/bin/python3
""" default entry point for the application
    """
from api.v1.views import app_views
from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from models import storage
from os import getenv

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ closes the session """
    storage.close()


@app.errorhandler(404)
def not_found(exception):
    """ returns a 404 error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    """launches the app"""
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
