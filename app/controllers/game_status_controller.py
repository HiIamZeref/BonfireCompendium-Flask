from flask import Blueprint, jsonify
from app.services.game_status_service import GameStatusService
from app.schemas.game_status_schema import GameStatusSchema

"""
Game Status Controller

This module defines the routes and request handlers for game status-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data serialization.

Routes:
-------
GET /<int:game_status_id>:
    Get a game status by its ID.
    - Parameters:
        - game_status_id (int): The ID of the game status to retrieve.
    - Responses:
        - 200: Game status found and returned successfully.
        - 404: Game status not found.

GET /:
    Get all game statuses.
    - Responses:
        - 200: All game statuses returned successfully.

Attributes:
-----------
game_statuses : Blueprint
    The Blueprint instance for game status routes.

Methods:
--------
get_game_status(game_status_id: int, game_status_service: GameStatusService = GameStatusService()) -> Response:
    Get a game status by ID.

get_all_game_statuses(game_status_service: GameStatusService = GameStatusService()) -> Response:    
    Get all game statuses.
"""

# Blueprint for game statuses
game_statuses = Blueprint('game_statuses', __name__)

# Game Status Controller Routes
def get_game_status(game_status_id, game_status_service: GameStatusService = GameStatusService()):
    """Get a game status by ID."""
    game_status = game_status_service.get(game_status_id)
    if not game_status:
        return jsonify({'message': 'Game status not found'}), 404

    return jsonify(GameStatusSchema().dump(game_status)), 200

def get_all_game_statuses(game_status_service: GameStatusService = GameStatusService()):
    """Get all game statuses."""
    game_statuses = game_status_service.get_all()
    return jsonify(GameStatusSchema(many=True).dump(game_statuses)), 200

# Register routes
game_statuses.add_url_rule('/<int:game_status_id>', view_func=get_game_status, methods=['GET'])
game_statuses.add_url_rule('/', view_func=get_all_game_statuses, methods=['GET'])