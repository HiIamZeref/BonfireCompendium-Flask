from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.game_schema import GameSchema
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
@games.route('/<int:game_id>', methods=['GET'])
def get_game(game_id, game_service: GameService = GameService()):
    """Get a game by ID."""
    game = game_service.get(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404

    return jsonify(GameSchema().dump(game)), 200

@games.route('/', methods=['GET'])
def get_all_games(game_service: GameService = GameService()):
    """Get all games."""
    games = game_service.get_all()
    return jsonify(GameSchema(many=True).dump(games)), 200

@games.route('/title', methods=['GET'])
def get_games_by_title(game_service: GameService = GameService()):
    """Get games by its title."""
    title = request.get_json().get('title')
    game = game_service.get_by_title(title)
    if not game:
        return jsonify({'message': 'Game not found'}), 404

    return jsonify(GameSchema(many= True).dump(game)), 200