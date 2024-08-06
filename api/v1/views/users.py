#!/usr/bin/python3
"""
    Default REST API actions for User objects.
"""
from flask import abort, request, jsonify
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """Gets the list of all Users."""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Gets a specific User by ID."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User by ID."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a new User."""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    data = request.get_json()
    if not data:
        return abort(400, 'Not a JSON')
    if 'email' not in data:
        return abort(400, 'Missing email')
    if 'password' not in data:
        return abort(400, 'Missing password')
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User by ID."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    data = request.get_json()
    if not data:
        return abort(400, 'Not a JSON')
    ignore_keys = ['id', 'created_at', 'updated_at', 'email']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
