from flask import Blueprint, jsonify, request
from app.services.follower_service import FollowerService
from app.schemas.follower_schema import FollowerSchema, CreateOrDeleteFollowerSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

# Blueprint for followers
followers = Blueprint('followers', __name__)

# Follower Controller Routes
@followers.route('/follow', methods=['POST'])
@jwt_required()
def follow(follower_service: FollowerService = FollowerService()):
    """Follow a user."""
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
    """Unfollow a user."""
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
    """Get all followers for a given user."""
    followers = follower_service.get_followers(user_id)
    return jsonify(FollowerSchema(many=True).dump(followers)), 200

@followers.route('/following/<int:follower_id>', methods=['GET'])
def get_following(follower_id, follower_service: FollowerService = FollowerService()):
    """Get all users that a given user is following."""
    following = follower_service.get_following(follower_id)
    return jsonify(FollowerSchema(many=True).dump(following)), 200
