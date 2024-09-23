from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.services.user_backlog_service import UserBacklogService
from app.schemas.user_backlog_schema import UserBacklogSchema, CreateOrDeleteUserBacklogSchema
from flask_jwt_extended import jwt_required


"""
User Backlog Controller

This module defines the routes and request handlers for user backlog-related operations.
It uses Flask's Blueprint to organize the routes, Marshmallow for data validation, and Flask-JWT-Extended for authentication.

Routes:
-------
GET /:
    Get a user backlog entry by user_id and game_id.
    - Authentication: Not required.
    - Request Body Parameters:
        - user_id (int): The ID of the user.
        - game_id (int): The ID of the game.
    - Responses:
        - 200: User backlog entry found and returned successfully.
        - 404: User backlog entry not found.

POST /:
    Create a new user backlog entry.
    - Authentication: Required (JWT).
    - Request Body Parameters:
        - user_id (int): The ID of the user.
        - game_id (int): The ID of the game.
    - Responses:
        - 201: User backlog entry created successfully.
        - 400: Validation error in the request body.

DELETE /:
    Delete a user backlog entry.
    - Authentication: Required (JWT).
    - Request Body Parameters:
        - user_id (int): The ID of the user.
        - game_id (int): The ID of the game.
    - Responses:
        - 204: User backlog entry deleted successfully.
        - 404: User backlog entry not found.

GET /<int:user_id>:
    Get all games in a user's backlog.
    - Authentication: Not required.
    - Path Parameters:
        - user_id (int): The ID of the user.
    - Responses:
        - 200: List of all games in the user's backlog returned successfully.

Attributes:
-----------
user_backlogs : Blueprint
    The Blueprint instance for user backlog routes.

Methods:
--------
get_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()) -> Response:
    Get a user backlog entry by user_id and game_id.

create_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()) -> Response:
    Create a new user backlog entry.

delete_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()) -> Response:
    Delete a user backlog entry.

get_user_backlog_list(user_id: int, user_backlog_service: UserBacklogService = UserBacklogService()) -> Response:
    Get all games in a user's backlog.
"""

# User Backlog Blueprint
user_backlogs = Blueprint('user_backlog', __name__)

# User Backlog Controller Routes
@user_backlogs.route('/', methods=['GET'])
def get_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()):
    """
    Get a user backlog entry.

    This route retrieves a specific user backlog entry based on the user ID and game ID.

    Authentication: Not required.

    Request Body Parameters:
    ------------------------
    user_id : int
        The ID of the user.
    game_id : int
        The ID of the game.

    Returns:
    --------
    Response
        JSON response containing the user backlog entry if found, or a 404 error message if not found.
    """
    data = request.get_json()
    user_id, game_id = data.get('user_id'), data.get('game_id')
    user_backlog = user_backlog_service.get(user_id, game_id)
    if not user_backlog:
        return jsonify({'message': 'User backlog entry not found'}), 404

    return jsonify(UserBacklogSchema().dump(user_backlog)), 200

@user_backlogs.route('/', methods=['POST'])
@jwt_required()
def create_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()):
    """
    Create a user backlog entry.

    This route creates a new backlog entry for the specified user and game.

    Authentication: Required (JWT).

    Request Body Parameters:
    ------------------------
    user_id : int
        The ID of the user.
    game_id : int
        The ID of the game.

    Returns:
    --------
    Response
        JSON response containing the created backlog entry, or a 400 error if validation fails.
    """
    data = request.get_json()
    create_user_backlog_schema = CreateOrDeleteUserBacklogSchema()

    try:
        validated_data = create_user_backlog_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user_backlog = user_backlog_service.create(validated_data)

    return jsonify(UserBacklogSchema().dump(user_backlog)), 201

@user_backlogs.route('/', methods=['DELETE'])
@jwt_required()
def delete_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()):
    """
    Delete a user backlog entry.

    This route deletes a backlog entry based on the provided user ID and game ID.

    Authentication: Required (JWT).

    Request Body Parameters:
    ------------------------
    user_id : int
        The ID of the user.
    game_id : int
        The ID of the game.

    Returns:
    --------
    Response
        A success message if the backlog entry is deleted, or a 404 error if not found.
    """
    data = request.get_json()
    delete_user_backlog_schema = CreateOrDeleteUserBacklogSchema()

    try:
        validated_data = delete_user_backlog_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user_backlog = user_backlog_service.get(validated_data.get('user_id'), validated_data.get('game_id'))
    if not user_backlog:
        return jsonify({'message': 'User backlog entry not found'}), 404

    user_backlog_service.delete(user_backlog)

    return jsonify({'message': 'User backlog entry deleted successfully'}), 204

@user_backlogs.route('/<int:user_id>', methods=['GET'])
def get_user_backlog_list(user_id, user_backlog_service: UserBacklogService = UserBacklogService()):
    """
    Get all games in a user's backlog.

    This route retrieves a list of all games that a specific user has in their backlog.

    Authentication: Not required.

    Path Parameters:
    ----------------
    user_id : int
        The ID of the user whose backlog will be retrieved.

    Returns:
    --------
    Response
        JSON response containing a list of games in the user's backlog.
    """
    user_backlog = user_backlog_service.get_backlog(user_id)
    return jsonify(UserBacklogSchema(many=True).dump(user_backlog)), 200
