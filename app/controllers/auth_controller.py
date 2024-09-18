from flask import Blueprint, jsonify, request
from app.services.auth_service import AuthService
from app.schemas.auth_schema import LoginSchema, AuthSchema
from marshmallow import ValidationError
from flask_jwt_extended import get_jwt_identity, jwt_required

"""
Auth Controller

This module defines the routes and request handlers for authentication-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data validation and serialization.

Routes:
-------
POST /login:
    Login a user.
    - Request Body:
        - username (str): The username of the user.
        - password (str): The password of the user.
    - Responses:
        - 200: User logged in successfully, returns the authentication token.
        - 400: Invalid credentials provided.

POST /refresh:
    Refresh the access token.
    - Headers:
        - Authorization: Bearer <refresh_token>
    - Responses:
        - 200: Access token refreshed successfully, returns the new access token.
        - 401: Invalid or expired refresh token.

Attributes:
-----------
auth : Blueprint
    The Blueprint instance for authentication routes.
"""

# Blueprint for authentication
auth = Blueprint('auth', __name__)

# Auth Controller Routes
@auth.route('/login', methods=['POST'])
def login(auth_service: AuthService = AuthService()):
    """
    Login a user.

    This route handles user login by validating the provided credentials and returning an authentication token.

    Parameters:
    -----------
    auth_service : AuthService, optional
        The authentication service instance (default is a new instance of AuthService).

    Request Body:
    -------------
    username : str
        The username of the user.
    password : str
        The password of the user.

    Returns:
    --------
    Response
        JSON response containing the authentication token if login is successful, or an error message if credentials are invalid.
    """

    data = request.get_json()
    login_schema = LoginSchema()
    auth_schema = AuthSchema()

    try:
        validated_data = login_schema.load(data)
    except ValidationError as err:
        return jsonify({'message': 'Invalid credentials'}), 400
    
    auth_status = auth_service.login(validated_data.get('username'), validated_data.get('password'))

    try:
        response = auth_schema.load(auth_status)
    except ValidationError as err:
        return jsonify(auth_status), 400
    
    return jsonify(response), 200


@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh(auth_service: AuthService = AuthService()):
    """
    Refresh the access token.

    This route handles refreshing the access token using a valid refresh token.

    Parameters:
    -----------
    auth_service : AuthService, optional
        The authentication service instance (default is a new instance of AuthService).

    Headers:
    --------
    Authorization : str
        The refresh token in the format 'Bearer <refresh_token>'.

    Returns:
    --------
    Response
        JSON response containing the new access token if the refresh token is valid, or an error message if the token is invalid or expired.
    """
    current_user_id = get_jwt_identity()
    new_access_token = auth_service.refresh(current_user_id)
    return jsonify(new_access_token), 200


@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout(auth_service: AuthService = AuthService()):
    """
    Logout the current user.

    This route handles logging out the current user by revoking the access token.

    Parameters:
    -----------
    auth_service : AuthService, optional
        The authentication service instance (default is a new instance of AuthService).

    Returns:
    --------
    Response
        JSON response indicating whether the logout was successful.

    """
    auth_service.logout()
    return jsonify({'message': 'Logout successful!'}), 200


