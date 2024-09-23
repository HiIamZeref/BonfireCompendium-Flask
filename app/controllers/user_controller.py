from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema, CreateOrDeleteUserSchema, ChangeUserPasswordSchema
from app.services.user_service import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity


"""
User Controller

This module defines the routes and request handlers for user-related operations.
It uses Flask's Blueprint to organize the routes, Marshmallow for data validation, and Flask-JWT-Extended for authentication.

Routes:
-------
POST /:
    Create a new user.
    - Authentication: Not required.
    - Request Body Parameters:
        - username (str): The username for the new user.
        - password (str): The password for the new user.
    - Responses:
        - 201: User created successfully.
        - 400: Validation error in the request body.

GET /<int:user_id>:
    Get a user by ID.
    - Authentication: Not required.
    - Path Parameters:
        - user_id (int): The ID of the user to retrieve.
    - Responses:
        - 200: User found and returned successfully.
        - 404: User not found.

GET /:
    Get all users.
    - Authentication: Not required.
    - Responses:
        - 200: List of all users returned successfully.

PATCH /:
    Update a user.
    - Authentication: Required (JWT).
    - Request Body Parameters:
        - Various user fields to be updated.
    - Responses:
        - 200: User updated successfully.
        - 400: Validation error in the request body.
        - 404: User not found.

PATCH /change_password:
    Change a user's password.
    - Authentication: Required (JWT).
    - Request Body Parameters:
        - old_password (str): The current password of the user.
        - new_password (str): The new password for the user.
    - Responses:
        - 200: Password changed successfully.
        - 400: Validation error in the request body.
        - 404: User not found.

DELETE /<int:user_id>:
    Delete a user by ID.
    - Authentication: Required (JWT).
    - Path Parameters:
        - user_id (int): The ID of the user to delete.
    - Responses:
        - 204: User deleted successfully.
        - 404: User not found.

Attributes:
-----------
users : Blueprint
    The Blueprint instance for user routes.

Methods:
--------
create_user(user_service: UserService = UserService()) -> Response:
    Create a new user.

get_user(user_id: int, user_service: UserService = UserService()) -> Response:
    Get a user by ID.

get_all_users(user_service: UserService = UserService()) -> Response:
    Get all users.

update_user(user_id: int, user_service: UserService = UserService()) -> Response:
    Update a user.

change_password(user_service: UserService = UserService()) -> Response:
    Change a user's password.

delete_user(user_id: int, user_service: UserService = UserService()) -> Response:
    Delete a user by ID.
"""

# Blueprint for users
users = Blueprint('users', __name__)

# User Controller Routes
@users.route('/', methods=['POST'])
def create_user(user_service: UserService = UserService()):
    """
    Create a new user.

    This route creates a new user using the provided data.

    Authentication: Not required.

    Request Body Parameters:
    ------------------------
    username : str
        The username for the new user.
    password : str
        The password for the new user.

    Returns:
    --------
    Response
        JSON response containing the created user, or a 400 error if validation fails.
    """
    data = request.get_json()
    user_schema = CreateOrDeleteUserSchema()

    try:
        validated_data = user_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user = user_service.create(validated_data)
    return jsonify(UserSchema().dump(user)), 201

@users.route('/<int:user_id>', methods=['GET'])
def get_user(user_id, user_service: UserService = UserService()):
    """
    Get a user by ID.

    This route retrieves a user by their unique ID.

    Authentication: Not required.

    Path Parameters:
    ----------------
    user_id : int
        The ID of the user to retrieve.

    Returns:
    --------
    Response
        JSON response containing the user details if found, or a 404 error message if not found.
    """
    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(UserSchema().dump(user)), 200

@users.route('/', methods=['GET'])
def get_all_users(user_service: UserService = UserService()):
    """
    Get all users.

    This route retrieves a list of all registered users.

    Authentication: Not required.

    Returns:
    --------
    Response
        JSON response containing a list of all users.
    """
    users = user_service.get_all() 
    return jsonify(UserSchema(many=True).dump(users)), 200

@users.route('/', methods=['PATCH'])
@jwt_required()
def update_user(user_id, user_service: UserService = UserService()):
    """
    Update a user.

    This route updates the details of the authenticated user.

    Authentication: Required (JWT).

    Request Body Parameters:
    ------------------------
    Various user fields to update (e.g., username, email).

    Returns:
    --------
    Response
        JSON response containing the updated user, or a 400 error if validation fails, or 404 if the user is not found.
    """
    user_id = get_jwt_identity()
    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    user_schema = UserSchema(partial=True)

    try:
        validated_data = user_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    updated_user = user_service.update(user, validated_data)
    return jsonify(user_schema.dump(updated_user)), 200

@users.route('/change_password', methods=['PATCH'])
@jwt_required()
def change_password(user_service: UserService = UserService()):
    """
    Change a user's password.

    This route allows the authenticated user to change their password.

    Authentication: Required (JWT).

    Request Body Parameters:
    ------------------------
    old_password : str
        The current password of the user.
    new_password : str
        The new password for the user.

    Returns:
    --------
    Response
        JSON response indicating the success or failure of the password change.
    """
    user_id = get_jwt_identity()
    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    password_schema = ChangeUserPasswordSchema()

    try:
        validated_data = password_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    response = user_service.change_password(user, validated_data)
    return jsonify(response), 200

@users.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id, user_service: UserService = UserService()):
    """
    Delete a user.

    This route deletes a user by their unique ID.

    Authentication: Required (JWT).

    Path Parameters:
    ----------------
    user_id : int
        The ID of the user to delete.

    Returns:
    --------
    Response
        A success message if the user is deleted, or a 404 error if not found.
    """
    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_service.delete(user)
    return jsonify({'message': 'User deleted successfully'}), 204
