#!/usr/bin/python3
"""default rest api actions for user objects."""
from flask import abort, request, jsonify
from api.v1.views import app_views
from models import storage
from models.user import User

@app_views.route('/users', strict_slashes=False)
def get_all_users():
    """ get the list of all users """
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<string:user_id>', strict_slashes=False)
def get_user(user_id):
    """ get a specific user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<string:user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ delete a user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ create a new user """
    if not request.is_json:
        return abort(400, 'Not a JSON')
    data = request.get_json()
    if 'email' not in data:
        return abort(400, 'Missing email')
    if 'password' not in data:
        return abort(400, 'Missing password')
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route('/users/<string:user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ update a user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.is_json:
        return abort(400, 'Not a JSON')
    data = request.get_json()
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
