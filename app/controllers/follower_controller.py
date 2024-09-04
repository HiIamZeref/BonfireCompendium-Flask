from flask import Blueprint, jsonify, request
from app.services.follower_service import FollowerService
from app.schemas.follower_schema import FollowerSchema

# Blueprint for followers
followers = Blueprint('followers', __name__)

# Follower Controller Routes
def follow(follower_service: FollowerService = FollowerService()):
    """Follow a user."""
    data = request.get_json()
    follower = follower_service.follow(data)
    return jsonify(FollowerSchema().dump(follower)), 201

def unfollow(follower_service: FollowerService = FollowerService()):
    """Unfollow a user."""
    data = request.get_json()
    follower_service.unfollow(data)
    return jsonify({'message': 'Unfollowed successfully'}), 200

def get_followers(user_id, follower_service: FollowerService = FollowerService()):
    """Get all followers for a given user."""
    followers = follower_service.get_followers(user_id)
    return jsonify(FollowerSchema(many=True).dump(followers)), 200

def get_following(follower_id, follower_service: FollowerService = FollowerService()):
    """Get all users that a given user is following."""
    following = follower_service.get_following(follower_id)
    return jsonify(FollowerSchema(many=True).dump(following)), 200

# Register routes
followers.add_url_rule('/follow', view_func=follow, methods=['POST'])
followers.add_url_rule('/unfollow', view_func=unfollow, methods=['DELETE'])
followers.add_url_rule('/<int:user_id>', view_func=get_followers, methods=['GET'])
followers.add_url_rule('/following/<int:follower_id>', view_func=get_following, methods=['GET'])