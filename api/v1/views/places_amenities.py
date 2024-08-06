#!/usr/bin/python3
"""default rest api actions for state objects.
    """
from flask import abort, request, jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.place import Place


@app_views.route('/places/<place_id>/amenities',
                 strict_slashes=False, methods=['GET'])
def get_all_place_amenities(place_id):
    """gets all available amenities of a place"""
    place = storage.get(Place, place_id)
    if not place:
        return abort(404)
    amenities = [amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 strict_slashes=False, methods=['GET'])
def delete_place_amenity(place_id, amenity_id):
    """deletes an amenity of a space"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return {}, 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def connect_amenity(place_id, amenity_id):
    """connects a place with an amenity"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if amenity in place.amenities:
        return {}, 200
    place.amenities.append(amenity)
    storage.save()
    return {}, 200
