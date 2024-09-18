from flask import Blueprint, request, jsonify
from app.services.game_platform_service import GamePlatformService
from app.schemas.game_platform_schema import GamePlatformSchema, CreateOrDeleteGamePlatform
from marshmallow import ValidationError

# Blueprint for game platforms
game_platforms = Blueprint('game_platforms', __name__)

# Game Platform Controller Routes
@game_platforms.route('/games/<int:game_id>', methods=['GET'])
def get_platform_by_game(game_id: int, game_platform_service: GamePlatformService = GamePlatformService()):
    """Get all platforms for a given game."""
    platforms = game_platform_service.get_platform_by_game(game_id)
    return jsonify(GamePlatformSchema(many=True).dump(platforms)), 200

@game_platforms.route('/platforms/<int:platform_id>', methods=['GET'])
def get_game_by_platform(platform_id: int, game_platform_service: GamePlatformService = GamePlatformService()):
    """Get all games for a given platform."""
    games = game_platform_service.get_game_by_platform(platform_id)
    return jsonify(GamePlatformSchema(many=True).dump(games)), 200