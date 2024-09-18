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
GET /<int:genre_id>:
    Get a genre by its ID.
    - Parameters:
        - genre_id (int): The ID of the genre to retrieve.
    - Responses:
        - 200: Genre found and returned successfully.
        - 404: Genre not found.

GET /:
    Get all genres.
    - Responses:
        - 200: All genres returned successfully.

Attributes:
-----------
genres : Blueprint
    The Blueprint instance for genre routes.

Methods:
--------
get_genre(genre_id: int, genre_service: GenreService = GenreService()) -> Response:
    Get a genre by ID.

get_all_genres(genre_service: GenreService = GenreService()) -> Response:
    Get all genres.
"""

# Blueprint for genres
genres = Blueprint('genres', __name__)

# Genre Controller Routes
@genres.route('/<int:genre_id>', methods=['GET'])
def get_genre(genre_id, genre_service: GenreService = GenreService()):
    """Get a genre by ID."""
    genre = genre_service.get(genre_id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404

    return jsonify(GenreSchema().dump(genre)), 200

@genres.route('/', methods=['GET'])
def get_all_genres(genre_service: GenreService = GenreService()):
    """Get all genres."""
    genres = genre_service.get_all()
    return jsonify(GenreSchema(many=True).dump(genres)), 200
