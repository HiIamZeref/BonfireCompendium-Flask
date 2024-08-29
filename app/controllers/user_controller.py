from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema
from app.services.user_service import UserService




# Blueprint for users
users = Blueprint('users', __name__)

# Dependency injection with Flask-Injector

def create_user(user_service: UserService = UserService()):
    """Create a new user."""
    data = request.get_json()
    user_schema = UserSchema()

    try:
        validated_data = user_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user = user_service.create(validated_data)
    return jsonify(user_schema.dump(user)), 201


def get_user(user_id, user_service: UserService = UserService()):
    """Get a user by ID."""
    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(UserSchema().dump(user)), 200


def get_all_users(user_service: UserService = UserService()):
    """Get all users."""
    users = user_service.get_all()  # This line expects user_service to be an instance of UserService
    return jsonify(UserSchema(many=True).dump(users)), 200


def update_user(user_id, user_service: UserService = UserService()):
    """Update a user."""
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


def delete_user(user_id, user_service: UserService = UserService()):
    """Delete a user."""
    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_service.delete(user)
    return jsonify({'message': 'User deleted successfully'}), 204

# Registering routes to the blueprint
users.add_url_rule('/', 'create_user', create_user, methods=['POST'])
users.add_url_rule('/<int:user_id>', 'get_user', get_user, methods=['GET'])
users.add_url_rule('/', 'get_all_users', get_all_users, methods=['GET'])
users.add_url_rule('/<int:user_id>', 'update_user', update_user, methods=['PATCH'])
users.add_url_rule('/<int:user_id>', 'delete_user', delete_user, methods=['DELETE'])
