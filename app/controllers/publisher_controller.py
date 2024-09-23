from flask import Blueprint, jsonify
from app.schemas.publisher_schema import PublisherSchema
from app.services.publisher_service import PublisherService


"""
Publisher Controller

This module defines the routes and request handlers for publisher-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data serialization.

Routes:
-------
GET /<int:publisher_id>:
    Get a publisher by its ID.
    - Parameters:
        - publisher_id (int): The ID of the publisher to retrieve.
    - Responses:
        - 200: Publisher found and returned successfully.
        - 404: Publisher not found.

GET /:
    Get all publishers.
    - Responses:
        - 200: All publishers returned successfully.

Attributes:
-----------
publishers : Blueprint
    The Blueprint instance for publisher routes.

Methods:
--------
get_publisher(publisher_id: int, publisher_service: PublisherService = PublisherService()) -> Response:
    Get a publisher by ID.

get_all_publishers(publisher_service: PublisherService = PublisherService()) -> Response:
    Get all publishers.
"""

# Blueprint for publishers
publishers = Blueprint('publishers', __name__)

# Publisher Controller Routes
@publishers.route('/<int:publisher_id>', methods=['GET'])
def get_publisher(publisher_id, publisher_service: PublisherService = PublisherService()):
    """
    Get a publisher by ID.

    This route retrieves a publisher using its unique ID.

    Authentication: Not required.

    Parameters:
    -----------
    publisher_id : int
        The ID of the publisher to retrieve.
    publisher_service : PublisherService, optional
        The publisher service instance (default is a new instance of PublisherService).

    Returns:
    --------
    Response
        JSON response containing the publisher details if found, or a 404 error message if not found.
    """
    publisher = publisher_service.get(publisher_id)
    if not publisher:
        return jsonify({'message': 'Publisher not found'}), 404

    return jsonify(PublisherSchema().dump(publisher)), 200

@publishers.route('/', methods=['GET'])
def get_all_publishers(publisher_service: PublisherService = PublisherService()):
    """
    Get all publishers.

    This route retrieves a list of all available publishers.

    Authentication: Not required.

    Parameters:
    -----------
    publisher_service : PublisherService, optional
        The publisher service instance (default is a new instance of PublisherService).

    Returns:
    --------
    Response
        JSON response containing a list of all publishers.
    """
    publishers = publisher_service.get_all()
    return jsonify(PublisherSchema(many=True).dump(publishers)), 200