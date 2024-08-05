#!/usr/bin/python3
"""places reviews"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.review import Review
from models.user import User
from models.place import Place

@app_views.route('/places/place_id/reviews', strict_slashes=False)
def get_reviews(place_id):
    """get a list of reviews"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    reviews = []
    for review in place.reviews:
        reviews.append(review.to_dict())
    return jsonify([review])


@app_views.route('/reviews/review_id', strict_slashes=False)
def get_review(review_id):
    """get a specific review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/places/<place_id>/reviews', methods=['DELETE'],
                 strict_slashes=False)
def delete_reviews(review_id):
    """delete review based on review_id"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """create a new review"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    if "user_id" not in data:
        return jsonify({"error": "Missing user_id"}), 400
    if 'text' not in data:
        return jsonify({"error": "Missing text"}), 400
    data['place_id'] = place_id
    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """update a review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    ignore_key = ['id', 'user_id', 'place_id',
                        'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_key:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict())
