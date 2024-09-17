from flask import Blueprint, request, jsonify
from app.services.game_platform_service import GamePlatformService
from app.schemas.game_platform_schema import GamePlatformSchema, CreateOrDeleteGamePlatform
from marshmallow import ValidationError

# Blueprint for game platforms
game_platforms = Blueprint('game_platforms', __name__)

# Game Platform Controller Routes
def create_game_platform(game_platform_service: GamePlatformService = GamePlatformService()):
    """Create a game platform."""
    data = request.get_json()
    create_game_platform_schema = CreateOrDeleteGamePlatform()

    try:
        validated_data = create_game_platform_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    game_platform = game_platform_service.create_game_platform(validated_data['game_id'], validated_data['platform_id'])

    if 'message' in game_platform:
        return jsonify(game_platform), 400

    return jsonify(GamePlatformSchema().dump(game_platform)), 201

def delete_game_platform(game_platform_service: GamePlatformService = GamePlatformService()):
    """Delete a game platform."""
    data = request.get_json()
    delete_game_platform_schema = CreateOrDeleteGamePlatform()

    try:
        validated_data = delete_game_platform_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    game_platform = game_platform_service.delete_game_platform(validated_data['game_id'], validated_data['platform_id'])

    if 'message' in game_platform:
        return jsonify(game_platform), 404

    return jsonify({'message': 'Game platform deleted successfully.'}), 204

def get_platform_by_game(game_id: int, game_platform_service: GamePlatformService = GamePlatformService()):
    """Get all platforms for a given game."""
    platforms = game_platform_service.get_platform_by_game(game_id)
    return jsonify(GamePlatformSchema(many=True).dump(platforms)), 200

def get_game_by_platform(platform_id: int, game_platform_service: GamePlatformService = GamePlatformService()):
    """Get all games for a given platform."""
    games = game_platform_service.get_game_by_platform(platform_id)
    return jsonify(GamePlatformSchema(many=True).dump(games)), 200


# Register routes
game_platforms.add_url_rule('/', view_func=create_game_platform, methods=['POST'])
game_platforms.add_url_rule('/', view_func=delete_game_platform, methods=['DELETE'])
game_platforms.add_url_rule('/games/<int:game_id>', view_func=get_platform_by_game, methods=['GET'])
game_platforms.add_url_rule('/platforms/<int:platform_id>', view_func=get_game_by_platform, methods=['GET'])