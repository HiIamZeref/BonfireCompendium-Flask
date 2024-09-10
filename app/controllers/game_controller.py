from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.user_schema import GameSchema
from app.services.game_service import GameService


"""
Game Controller

This module defines the routes and request handlers for game-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data serialization.

Routes:
-------
GET /<int:game_id>:
    Get a game by its ID.
    - Parameters:
        - game_id (int): The ID of the game to retrieve.
    - Responses:
        - 200: Game found and returned successfully.
        - 404: Game not found.

GET /:
    Get a list of all games.
    - Responses:
        - 200: List of games returned successfully.

GET /title:
    Get a game by its title.
    - Parameters:
        - title (str): The title of the game to retrieve.
    - Responses:
        - 200: Game found and returned successfully.
        - 404: Game not found.

Attributes:
-----------
games : Blueprint
    The Blueprint instance for game routes.
"""

# Games Blueprint
games = Blueprint('games', __name__)

# Games Controller Routes
def get_game(game_id, game_service: GameService = GameService()):
    """Get a game by ID."""
    game = game_service.get(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404

    return jsonify(GameSchema().dump(game)), 200

def get_all_games(game_service: GameService = GameService()):
    """Get all games."""
    games = game_service.get_all()
    return jsonify(GameSchema(many=True).dump(games)), 200

def get_game_by_title(title, game_service: GameService = GameService()):
    """Get a game by its title."""
    game = game_service.get_by_title(title)
    if not game:
        return jsonify({'message': 'Game not found'}), 404

    return jsonify(GameSchema().dump(game)), 200

# Register routes
games.add_url_rule('/<int:game_id>', view_func=get_game, methods=['GET'])
games.add_url_rule('/', view_func=get_all_games, methods=['GET'])
games.add_url_rule('/title', view_func=get_game_by_title, methods=['GET'])