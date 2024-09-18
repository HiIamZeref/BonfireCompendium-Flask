from flask import Blueprint, jsonify, request
from app.services.follower_service import FollowerService
from app.schemas.follower_schema import FollowerSchema, CreateOrDeleteFollowerSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

"""
Follower Controller

This module defines the routes and request handlers for follower-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data validation and serialization.

Routes:
-------
POST /followers/follow:
    Follow a user.
    - Authentication: Required (JWT).
    - Request Body:
        - followed_id (int): The ID of the user to follow.
    - Responses:
        - 201: Successfully followed the user, returns the follower details.
        - 400: Validation error for input data.

DELETE /followers/unfollow:
    Unfollow a user.
    - Authentication: Required (JWT).
    - Request Body:
        - followed_id (int): The ID of the user to unfollow.
    - Responses:
        - 204: Successfully unfollowed the user, returns no content.
        - 400: Validation error for input data.
        - 404: Already unfollowed or user not found.

GET /followers/<int:user_id>:
    Get all followers for a given user.
    - Authentication: Not required.
    - Path Parameters:
        - user_id (int): The ID of the user whose followers are to be retrieved.
    - Responses:
        - 200: Successfully retrieved the list of followers.

GET /followers/following/<int:follower_id>:
    Get all users that a given user is following.
    - Authentication: Not required.
    - Path Parameters:
        - follower_id (int): The ID of the user whose following list is to be retrieved.
    - Responses:
        - 200: Successfully retrieved the list of users the given user is following.

Attributes:
-----------
followers : Blueprint
    The Blueprint instance for follower routes.
"""

# Blueprint for followers
followers = Blueprint('followers', __name__)

# Follower Controller Routes
@followers.route('/follow', methods=['POST'])
@jwt_required()
def follow(follower_service: FollowerService = FollowerService()):
    """
    Follow a user.

    This route allows the current user to follow another user by providing the followed user's ID.

    Authentication: Required (JWT).

    Parameters:
    -----------
    follower_service : FollowerService, optional
        The follower service instance (default is a new instance of FollowerService).

    Request Body:
    -------------
    followed_id : int
        The ID of the user to be followed.

    Returns:
    --------
    Response
        JSON response containing the follower details if the follow operation is successful, or validation errors if the input data is invalid.
    """
    data = request.get_json()
    create_follower_schema = CreateOrDeleteFollowerSchema()

    try:
        validated_data = create_follower_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    follower = follower_service.follow(validated_data)
    
    return jsonify(FollowerSchema().dump(follower)), 201

@followers.route('/unfollow', methods=['DELETE'])
@jwt_required()
def unfollow(follower_service: FollowerService = FollowerService()):
    """
    Unfollow a user.

    This route allows the current user to unfollow another user by providing the followed user's ID.

    Authentication: Required (JWT).

    Parameters:
    -----------
    follower_service : FollowerService, optional
        The follower service instance (default is a new instance of FollowerService).

    Request Body:
    -------------
    followed_id : int
        The ID of the user to be unfollowed.

    Returns:
    --------
    Response
        JSON response indicating successful unfollow or errors if the user was already unfollowed or if the input data is invalid.
    """
    data = request.get_json()
    follower_schema = CreateOrDeleteFollowerSchema()

    try:
        validated_data = follower_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    try:
        follower_service.unfollow(validated_data)
    except ValueError as err:
        return jsonify({'message': 'Already unfollowed.'}), 404
    
    return jsonify({'message': 'Unfollowed successfully'}), 204

@followers.route('/<int:user_id>', methods=['GET'])
def get_followers(user_id, follower_service: FollowerService = FollowerService()):
    """
    Get all followers for a given user.

    This route retrieves all the followers of a specific user based on the provided user ID.

    Authentication: Not required.

    Parameters:
    -----------
    user_id : int
        The ID of the user whose followers are to be retrieved.
    follower_service : FollowerService, optional
        The follower service instance (default is a new instance of FollowerService).

    Returns:
    --------
    Response
        JSON response containing a list of followers for the specified user.
    """
    followers = follower_service.get_followers(user_id)
    return jsonify(FollowerSchema(many=True).dump(followers)), 200

@followers.route('/following/<int:follower_id>', methods=['GET'])
def get_following(follower_id, follower_service: FollowerService = FollowerService()):
    """
    Get all users that a given user is following.

    This route retrieves all the users that a specific user is following based on the provided user ID.

    Authentication: Not required.

    Parameters:
    -----------
    follower_id : int
        The ID of the user whose following list is to be retrieved.
    follower_service : FollowerService, optional
        The follower service instance (default is a new instance of FollowerService).

    Returns:
    --------
    Response
        JSON response containing a list of users the specified user is following.
    """
    following = follower_service.get_following(follower_id)
    return jsonify(FollowerSchema(many=True).dump(following)), 200
