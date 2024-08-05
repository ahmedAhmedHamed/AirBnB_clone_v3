#!/usr/bin/python3
"""default rest api actions for city objects.
    """
from flask import abort, request, jsonify
from api.v1.views import app_views
from models import storage
from models.user import User

@app_views.route('/users', strict_slashes=False)
def get_all_users():
    """ get the list of all user
    """
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<string:user_id>', strict_slashes=False)
def get_user(user_id):
    """ get a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<string:user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """ delete a user
    """
    user = storage.get(User, user_id)
    if not user:
        return abort(404)
    else:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def create_user(user_id):
    """ create a new user
    """
    if request.content_type != 'application/json':
        return abort(400, 'NOT a JSON')
    if not request.get_json():
        return abort(400, 'NOT a JSON')
    data = request.get_json()
    if 'email' not in data:
        return abort(400, 'Missing email')
    if 'password' not in data:
        return abort(400, 'Missing password')
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 200


@app_views.route('/users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """ update a user
    """
    user = storage.get(User, user_id)
    if user:
        if not request.get_json():
            return abort(404, 'NOT a JSON')
        if request.content_type != 'application/json':
            return abort(404, 'NOT a JSON')
        data = request.get_json()
        ignore_key = ['id', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in ignore_key:
                setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict()), 200
    else:
        return abort(404)
