from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_injector import inject
from services import UserService
from schemas import UserSchema

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users', methods=['POST'])
@inject
def create_user(user_service: UserService):
    '''Create a new user'''

    data = request.get_json()
    user_schema = UserSchema()

    # Validate data
    try:
        validated_data = user_schema.load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    user = user_service.create(validated_data)
    return jsonify(user_schema.dump(user)), 201

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
@inject
def get_user(user_id, user_service: UserService):
    '''Get a user by id'''

    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    user_schema = UserSchema()
    return jsonify(user_schema.dump(user)), 200

@user_blueprint.route('/users', methods=['GET'])
@inject
def get_all_users(user_service: UserService):
    '''Get all users'''

    users = user_service.get_all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users)), 200

@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
@inject
def update_user(user_id, user_service: UserService):
    '''Update a user'''

    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    data = request.get_json()
    user_schema = UserSchema(partial=True)

    # Validate data
    try:
        validated_data = user_schema.load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    updated_user = user_service.update(user, validated_data)
    return jsonify(user_schema.dump(updated_user)), 200

@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
@inject
def delete_user(user_id, user_service: UserService):
    '''Delete a user'''

    user = user_service.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404
    
    user_service.delete(user)
    return jsonify({'message': 'User deleted successfully!'}), 204