from flask import Blueprint, jsonify
from app.services.game_status_service import GameStatusService
from app.schemas.game_status_schema import GameStatusSchema

"""
Game Status Controller

This module defines the routes and request handlers for game status-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data serialization.

Routes:
-------
GET /game_statuses/<int:game_status_id>:
    Get a game status by its ID.
    - Authentication: Not required.
    - Path Parameters:
        - game_status_id (int): The ID of the game status to retrieve.
    - Responses:
        - 200: Game status found and returned successfully.
        - 404: Game status not found.

GET /game_statuses/:
    Get a list of all game statuses.
    - Authentication: Not required.
    - Responses:
        - 200: All game statuses returned successfully.

Attributes:
-----------
game_statuses : Blueprint
    The Blueprint instance for game status routes.
"""

# Blueprint for game statuses
game_statuses = Blueprint('game_statuses', __name__)

# Game Status Controller Routes
@game_statuses.route('/<int:game_status_id>', methods=['GET'])
def get_game_status(game_status_id, game_status_service: GameStatusService = GameStatusService()):
    """
    Get a game status by ID.

    This route retrieves a game status using its unique ID.

    Authentication: Not required.

    Parameters:
    -----------
    game_status_id : int
        The ID of the game status to retrieve.
    game_status_service : GameStatusService, optional
        The game status service instance (default is a new instance of GameStatusService).

    Returns:
    --------
    Response
        JSON response containing the game status details if found, or a 404 error message if not found.
    """
    game_status = game_status_service.get(game_status_id)
    if not game_status:
        return jsonify({'message': 'Game status not found'}), 404

    return jsonify(GameStatusSchema().dump(game_status)), 200

@game_statuses.route('/', methods=['GET'])
def get_all_game_statuses(game_status_service: GameStatusService = GameStatusService()):
    """
    Get all game statuses.

    This route retrieves a list of all available game statuses.

    Authentication: Not required.

    Parameters:
    -----------
    game_status_service : GameStatusService, optional
        The game status service instance (default is a new instance of GameStatusService).

    Returns:
    --------
    Response
        JSON response containing a list of all game statuses.
    """
    game_statuses = game_status_service.get_all()
    return jsonify(GameStatusSchema(many=True).dump(game_statuses)), 200
