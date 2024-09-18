from flask import Blueprint, request, jsonify
from app.services.game_platform_service import GamePlatformService
from app.schemas.game_platform_schema import GamePlatformSchema, CreateOrDeleteGamePlatform
from marshmallow import ValidationError

"""
Game Platform Controller

This module defines the routes and request handlers for game-platform-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data validation and serialization.

Routes:
-------
GET /game_platforms/games/<int:game_id>:
    Get all platforms for a given game.
    - Authentication: Not required.
    - Path Parameters:
        - game_id (int): The ID of the game to retrieve platforms for.
    - Responses:
        - 200: List of platforms returned successfully.

GET /game_platforms/platforms/<int:platform_id>:
    Get all games for a given platform.
    - Authentication: Not required.
    - Path Parameters:
        - platform_id (int): The ID of the platform to retrieve games for.
    - Responses:
        - 200: List of games returned successfully.

Attributes:
-----------
game_platforms : Blueprint
    The Blueprint instance for game platform routes.
"""

# Blueprint for game platforms
game_platforms = Blueprint('game_platforms', __name__)

# Game Platform Controller Routes
@game_platforms.route('/games/<int:game_id>', methods=['GET'])
def get_platform_by_game(game_id: int, game_platform_service: GamePlatformService = GamePlatformService()):
    """
    Get all platforms for a given game.

    This route retrieves all platforms associated with a specific game by its ID.

    Authentication: Not required.

    Parameters:
    -----------
    game_id : int
        The ID of the game to retrieve platforms for.
    game_platform_service : GamePlatformService, optional
        The game platform service instance (default is a new instance of GamePlatformService).

    Returns:
    --------
    Response
        JSON response containing the list of platforms for the specified game.
    """
    platforms = game_platform_service.get_platform_by_game(game_id)
    return jsonify(GamePlatformSchema(many=True).dump(platforms)), 200

@game_platforms.route('/platforms/<int:platform_id>', methods=['GET'])
def get_game_by_platform(platform_id: int, game_platform_service: GamePlatformService = GamePlatformService()):
    """
    Get all games for a given platform.

    This route retrieves all games associated with a specific platform by its ID.

    Authentication: Not required.

    Parameters:
    -----------
    platform_id : int
        The ID of the platform to retrieve games for.
    game_platform_service : GamePlatformService, optional
        The game platform service instance (default is a new instance of GamePlatformService).

    Returns:
    --------
    Response
        JSON response containing the list of games for the specified platform.
    """
    games = game_platform_service.get_game_by_platform(platform_id)
    return jsonify(GamePlatformSchema(many=True).dump(games)), 200
