from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.services.user_backlog_service import UserBacklogService
from app.schemas.user_backlog_schema import UserBacklogSchema, CreateOrDeleteUserBacklogSchema



# User Backlog Blueprint
user_backlogs = Blueprint('user_backlog', __name__)

# User Backlog Controller Routes
def get_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()):
    """Get a user backlog entry."""
    data = request.get_json()
    user_id, game_id = data.get('user_id'), data.get('game_id')
    user_backlog = user_backlog_service.get(user_id, game_id)
    if not user_backlog:
        return jsonify({'message': 'User backlog entry not found'}), 404

    return jsonify(UserBacklogSchema().dump(user_backlog)), 200

def create_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()):
    """Create a user backlog entry."""
    data = request.get_json()
    create_user_backlog_schema = CreateOrDeleteUserBacklogSchema()

    try:
        validated_data = create_user_backlog_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user_backlog = user_backlog_service.create(validated_data)

    return jsonify(UserBacklogSchema().dump(user_backlog)), 201

def delete_user_backlog(user_backlog_service: UserBacklogService = UserBacklogService()):
    """Delete a user backlog entry."""
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

def get_user_backlog_list(user_id, user_backlog_service: UserBacklogService = UserBacklogService()):
    """Get all games in a user's backlog."""
    user_backlog = user_backlog_service.get_backlog(user_id)
    return jsonify(UserBacklogSchema(many=True).dump(user_backlog)), 200

# Register routes
user_backlogs.add_url_rule('/', view_func=get_user_backlog, methods=['GET'])
user_backlogs.add_url_rule('/', view_func=create_user_backlog, methods=['POST'])
user_backlogs.add_url_rule('/', view_func=delete_user_backlog, methods=['DELETE'])
user_backlogs.add_url_rule('/<int:user_id>', view_func=get_user_backlog_list, methods=['GET'])