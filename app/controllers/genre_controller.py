from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.genre_schema import GenreSchema
from app.services.genre_service import GenreService


"""
Genre Controller

This module defines the routes and request handlers for genre-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data serialization.

Routes:
-------
GET /genres/<int:genre_id>:
    Get a genre by its ID.
    - Authentication: Not required.
    - Path Parameters:
        - genre_id (int): The ID of the genre to retrieve.
    - Responses:
        - 200: Genre found and returned successfully.
        - 404: Genre not found.

GET /genres/:
    Get a list of all genres.
    - Authentication: Not required.
    - Responses:
        - 200: List of all genres returned successfully.

Attributes:
-----------
genres : Blueprint
    The Blueprint instance for genre routes.
"""

# Blueprint for genres
genres = Blueprint('genres', __name__)

# Genre Controller Routes
@genres.route('/<int:genre_id>', methods=['GET'])
def get_genre(genre_id, genre_service: GenreService = GenreService()):
    """
    Get a genre by ID.

    This route retrieves a genre using its unique ID.

    Authentication: Not required.

    Parameters:
    -----------
    genre_id : int
        The ID of the genre to retrieve.
    genre_service : GenreService, optional
        The genre service instance (default is a new instance of GenreService).

    Returns:
    --------
    Response
        JSON response containing the genre details if found, or a 404 error message if not found.
    """
    genre = genre_service.get(genre_id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404

    return jsonify(GenreSchema().dump(genre)), 200

@genres.route('/', methods=['GET'])
def get_all_genres(genre_service: GenreService = GenreService()):
    """
    Get all genres.

    This route retrieves a list of all available genres.

    Authentication: Not required.

    Parameters:
    -----------
    genre_service : GenreService, optional
        The genre service instance (default is a new instance of GenreService).

    Returns:
    --------
    Response
        JSON response containing a list of all genres.
    """
    genres = genre_service.get_all()
    return jsonify(GenreSchema(many=True).dump(genres)), 200
