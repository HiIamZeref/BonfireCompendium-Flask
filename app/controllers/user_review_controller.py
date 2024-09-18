from flask import Blueprint, jsonify, request
from app.schemas.user_review_schema import UserReviewSchema
from app.services.user_review_service import UserReviewService
from flask_jwt_extended import jwt_required, get_jwt_identity

# Blueprint for user reviews
user_reviews = Blueprint('user_reviews', __name__)

# User Review Controller Routes
@user_reviews.route('/<int:user_review_id>', methods=['GET'])
def get_user_review(user_review_id, user_review_service: UserReviewService = UserReviewService()):
    """Get a user review by ID."""
    user_review = user_review_service.get(user_review_id)
    if not user_review:
        return jsonify({'message': 'User review not found'}), 404

    return jsonify(UserReviewSchema().dump(user_review)), 200

@user_reviews.route('/', methods=['GET'])
def get_all_user_reviews(user_review_service: UserReviewService = UserReviewService()):
    """Get all user reviews."""
    user_reviews = user_review_service.get_all()
    return jsonify(UserReviewSchema(many=True).dump(user_reviews)), 200

@user_reviews.route('/', methods=['POST'])
@jwt_required()
def create_user_review(user_review_service: UserReviewService = UserReviewService()):
    """Create a new user review."""
    data = request.get_json()
    result = user_review_service.create(data)
    return jsonify(result), 201 if 'id' in result else 400

@user_reviews.route('/<int:user_review_id>', methods=['PUT'])
@jwt_required()
def update_user_review(user_review_id, user_review_service: UserReviewService = UserReviewService()):
    """Update a user review."""
    data = request.get_json()
    user_review = user_review_service.get(user_review_id)
    if not user_review:
        return jsonify({'message': 'User review not found'}), 404

    result = user_review_service.update(user_review, data)
    return jsonify(result), 200 if 'id' in result else 400

@user_reviews.route('/<int:user_review_id>', methods=['DELETE'])
@jwt_required()
def delete_user_review(user_review_id, user_review_service: UserReviewService = UserReviewService()):
    """Delete a user review."""
    user_review = user_review_service.get(user_review_id)
    if not user_review:
        return jsonify({'message': 'User review not found'}), 404

    result = user_review_service.delete(user_review)
    return jsonify(result), 200 if 'message' in result else 400

@user_reviews.route('/game/<int:game_id>', methods=['GET'])
def get_user_reviews_by_game(game_id, user_review_service: UserReviewService = UserReviewService()):
    """Get all user reviews for a specific game."""
    user_reviews = user_review_service.get_by_game(game_id)
    return jsonify(UserReviewSchema(many=True).dump(user_reviews)), 200

@user_reviews.route('/user/<int:user_id>', methods=['GET'])
def get_user_reviews_by_user(user_id, user_review_service: UserReviewService = UserReviewService()):
    """Get all user reviews by a specific user."""
    user_reviews = user_review_service.get_by_user(user_id)
    return jsonify(UserReviewSchema(many=True).dump(user_reviews)), 200
