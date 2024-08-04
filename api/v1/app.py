#!/usr/bin/python3
"""_summary_
    """
from flask import Flask
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


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
