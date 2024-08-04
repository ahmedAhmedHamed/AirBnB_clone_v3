#!/usr/bin/python3
""" default entry point for the application
    """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["0.0.0.0"])

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
