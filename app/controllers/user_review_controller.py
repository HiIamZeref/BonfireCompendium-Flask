from flask import Blueprint, jsonify, request
from app.schemas.user_review_schema import UserReviewSchema
from app.services.user_review_service import UserReviewService
from flask_jwt_extended import jwt_required, get_jwt_identity


"""
User Review Controller

This module defines the routes and request handlers for user review-related operations.
It uses Flask's Blueprint to organize the routes and Flask-JWT-Extended for authentication.

Routes:
-------
GET /<int:user_review_id>:
    Get a user review by its ID.
    - Authentication: Not required.
    - Path Parameters:
        - user_review_id (int): The ID of the user review to retrieve.
    - Responses:
        - 200: User review found and returned successfully.
        - 404: User review not found.

GET /:
    Get all user reviews.
    - Authentication: Not required.
    - Responses:
        - 200: All user reviews returned successfully.

POST /:
    Create a new user review.
    - Authentication: Required (JWT).
    - Request Body Parameters:
        - Data for the new review.
    - Responses:
        - 201: User review created successfully.
        - 400: Validation error in the request body.

PUT /<int:user_review_id>:
    Update a user review by its ID.
    - Authentication: Required (JWT).
    - Path Parameters:
        - user_review_id (int): The ID of the user review to update.
    - Request Body Parameters:
        - Data for updating the review.
    - Responses:
        - 200: User review updated successfully.
        - 404: User review not found.
        - 400: Validation error in the request body.

DELETE /<int:user_review_id>:
    Delete a user review by its ID.
    - Authentication: Required (JWT).
    - Path Parameters:
        - user_review_id (int): The ID of the user review to delete.
    - Responses:
        - 200: User review deleted successfully.
        - 404: User review not found.

GET /game/<int:game_id>:
    Get all user reviews for a specific game.
    - Authentication: Not required.
    - Path Parameters:
        - game_id (int): The ID of the game to retrieve reviews for.
    - Responses:
        - 200: List of user reviews for the game.

GET /user/<int:user_id>:
    Get all user reviews by a specific user.
    - Authentication: Not required.
    - Path Parameters:
        - user_id (int): The ID of the user whose reviews to retrieve.
    - Responses:
        - 200: List of reviews by the user.

Attributes:
-----------
user_reviews : Blueprint
    The Blueprint instance for user review routes.

Methods:
--------
get_user_review(user_review_id: int, user_review_service: UserReviewService = UserReviewService()) -> Response:
    Get a user review by its ID.

get_all_user_reviews(user_review_service: UserReviewService = UserReviewService()) -> Response:
    Get all user reviews.

create_user_review(user_review_service: UserReviewService = UserReviewService()) -> Response:
    Create a new user review.

update_user_review(user_review_id: int, user_review_service: UserReviewService = UserReviewService()) -> Response:
    Update a user review by its ID.

delete_user_review(user_review_id: int, user_review_service: UserReviewService = UserReviewService()) -> Response:
    Delete a user review by its ID.

get_user_reviews_by_game(game_id: int, user_review_service: UserReviewService = UserReviewService()) -> Response:
    Get all user reviews for a specific game.

get_user_reviews_by_user(user_id: int, user_review_service: UserReviewService = UserReviewService()) -> Response:
    Get all user reviews by a specific user.
"""

# Blueprint for user reviews
user_reviews = Blueprint('user_reviews', __name__)

# User Review Controller Routes
@user_reviews.route('/<int:user_review_id>', methods=['GET'])
def get_user_review(user_review_id, user_review_service: UserReviewService = UserReviewService()):
    """
    Get a user review by ID.

    This route retrieves a user review by its unique ID.

    Authentication: Not required.

    Path Parameters:
    ----------------
    user_review_id : int
        The ID of the user review to retrieve.

    Returns:
    --------
    Response
        JSON response containing the user review details if found, or a 404 error message if not found.
    """
    user_review = user_review_service.get(user_review_id)
    if not user_review:
        return jsonify({'message': 'User review not found'}), 404

    return jsonify(UserReviewSchema().dump(user_review)), 200

@user_reviews.route('/', methods=['GET'])
def get_all_user_reviews(user_review_service: UserReviewService = UserReviewService()):
    """
    Get all user reviews.

    This route retrieves a list of all user reviews.

    Authentication: Not required.

    Returns:
    --------
    Response
        JSON response containing a list of all user reviews.
    """
    user_reviews = user_review_service.get_all()
    return jsonify(UserReviewSchema(many=True).dump(user_reviews)), 200

@user_reviews.route('/', methods=['POST'])
@jwt_required()
def create_user_review(user_review_service: UserReviewService = UserReviewService()):
    """
    Create a new user review.

    This route creates a new user review based on the provided data.

    Authentication: Required (JWT).

    Request Body Parameters:
    ------------------------
    Data for the new user review.

    Returns:
    --------
    Response
        JSON response containing the created user review, or a 400 error if validation fails.
    """
    data = request.get_json()
    result = user_review_service.create(data)
    return jsonify(result), 201 if 'id' in result else 400

@user_reviews.route('/<int:user_review_id>', methods=['PUT'])
@jwt_required()
def update_user_review(user_review_id, user_review_service: UserReviewService = UserReviewService()):
    """
    Update a user review.

    This route updates the details of a user review by its unique ID.

    Authentication: Required (JWT).

    Path Parameters:
    ----------------
    user_review_id : int
        The ID of the user review to update.

    Request Body Parameters:
    ------------------------
    Data for updating the user review.

    Returns:
    --------
    Response
        JSON response containing the updated user review, or a 404 error if not found, or a 400 error if validation fails.
    """
    data = request.get_json()
    user_review = user_review_service.get(user_review_id)
    if not user_review:
        return jsonify({'message': 'User review not found'}), 404

    result = user_review_service.update(user_review, data)
    return jsonify(result), 200 if 'id' in result else 400

@user_reviews.route('/<int:user_review_id>', methods=['DELETE'])
@jwt_required()
def delete_user_review(user_review_id, user_review_service: UserReviewService = UserReviewService()):
    """
    Delete a user review.

    This route deletes a user review by its unique ID.

    Authentication: Required (JWT).

    Path Parameters:
    ----------------
    user_review_id : int
        The ID of the user review to delete.

    Returns:
    --------
    Response
        A success message if the user review is deleted, or a 404 error if not found.
    """
    user_review = user_review_service.get(user_review_id)
    if not user_review:
        return jsonify({'message': 'User review not found'}), 404

    result = user_review_service.delete(user_review)
    return jsonify(result), 200 if 'message' in result else 400

@user_reviews.route('/game/<int:game_id>', methods=['GET'])
def get_user_reviews_by_game(game_id, user_review_service: UserReviewService = UserReviewService()):
    """
    Get all user reviews for a specific game.

    This route retrieves all user reviews for a given game by the game's unique ID.

    Authentication: Not required.

    Path Parameters:
    ----------------
    game_id : int
        The ID of the game for which to retrieve reviews.

    Returns:
    --------
    Response
        JSON response containing a list of user reviews for the game.
    """
    user_reviews = user_review_service.get_by_game(game_id)
    return jsonify(UserReviewSchema(many=True).dump(user_reviews)), 200

@user_reviews.route('/user/<int:user_id>', methods=['GET'])
def get_user_reviews_by_user(user_id, user_review_service: UserReviewService = UserReviewService()):
    """
    Get all user reviews by a specific user.

    This route retrieves all reviews made by a specific user by the user's unique ID.

    Authentication: Not required.

    Path Parameters:
    ----------------
    user_id : int
        The ID of the user whose reviews to retrieve.

    Returns:
    --------
    Response
        JSON response containing a list of reviews made by the user.
    """
    user_reviews = user_review_service.get_by_user(user_id)
    return jsonify(UserReviewSchema(many=True).dump(user_reviews)), 200
