from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema, CreateOrDeleteUserSchema, ChangeUserPasswordSchema
from app.services.user_service import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity




# Blueprint for users
users = Blueprint('users', __name__)

# User Controller Routes
@users.route('/', methods=['POST'])
def create_user(user_service: UserService = UserService()):
    """Create a new user."""
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
    """Get a user by ID."""
    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(UserSchema().dump(user)), 200

@users.route('/', methods=['GET'])
def get_all_users(user_service: UserService = UserService()):
    """Get all users."""
    users = user_service.get_all() 
    return jsonify(UserSchema(many=True).dump(users)), 200

@users.route('/', methods=['PATCH'])
@jwt_required()
def update_user(user_id, user_service: UserService = UserService()):
    """Update a user."""
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
    """Change a user's password."""
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
    """Delete a user."""
    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_service.delete(user)
    return jsonify({'message': 'User deleted successfully'}), 204

