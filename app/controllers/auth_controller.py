from flask import Blueprint, jsonify, request
from app.services.auth_service import AuthService
from app.schemas.auth_schema import LoginSchema, AuthSchema
from marshmallow import ValidationError
from flask_jwt_extended import get_jwt_identity, jwt_required

# Blueprint for authentication
auth = Blueprint('auth', __name__)

# Auth Controller Routes
@auth.route('/login', methods=['POST'])
def login(auth_service: AuthService = AuthService()):
    """Login a user."""
    data = request.get_json()
    login_schema = LoginSchema()

    try:
        validated_data = login_schema.load(data)
    except ValidationError as err:
        return jsonify({'message': 'Invalid credentials'}), 400
    
    auth = auth_service.login(validated_data.get('username'), validated_data.get('password'))

    print(auth)
    
    return jsonify(AuthSchema().dump(auth))


@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh(auth_service: AuthService = AuthService()):
    """Refresh the access token."""
    current_user_id = get_jwt_identity()
    new_access_token = auth_service.refresh(current_user_id)
    return jsonify(new_access_token), 200


@auth.route('/logout', methods=['POST'])
@jwt_required(refresh=True)
def logout(auth_service: AuthService = AuthService()):
    """Logout the current user."""
    auth_service.logout()
    return jsonify({'message': 'Logout successful!'}), 200


