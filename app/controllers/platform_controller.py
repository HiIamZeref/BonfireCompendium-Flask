from flask import Blueprint, jsonify
from app.schemas.platform_schema import PlatformSchema
from app.services.platform_service import PlatformService


"""
Platform Controller

This module defines the routes and request handlers for platform-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data serialization.

Routes:
-------
GET /<int:platform_id>:
    Get a platform by its ID.
    - Parameters:
        - platform_id (int): The ID of the platform to retrieve.
    - Responses:
        - 200: Platform found and returned successfully.
        - 404: Platform not found.

GET /:
    Get all platforms.
    - Responses:
        - 200: All platforms returned successfully.

Attributes:
-----------
platforms : Blueprint
    The Blueprint instance for platform routes.

Methods:
--------
get_platform(platform_id: int, platform_service: PlatformService = PlatformService()) -> Response:
    Get a platform by ID.

get_all_platforms(platform_service: PlatformService = PlatformService()) -> Response:
    Get all platforms.
"""

# Blueprint for platforms
platforms = Blueprint('platforms', __name__)

# Platform Controller Routes
@platforms.route('/<int:platform_id>', methods=['GET'])
def get_platform(platform_id, platform_service: PlatformService = PlatformService()):
    """
    Get a platform by ID.

    This route retrieves a platform using its unique ID.

    Authentication: Not required.

    Parameters:
    -----------
    platform_id : int
        The ID of the platform to retrieve.
    platform_service : PlatformService, optional
        The platform service instance (default is a new instance of PlatformService).

    Returns:
    --------
    Response
        JSON response containing the platform details if found, or a 404 error message if not found.
    """
    platform = platform_service.get(platform_id)
    if not platform:
        return jsonify({'message': 'Platform not found'}), 404

    return jsonify(PlatformSchema().dump(platform)), 200

@platforms.route('/', methods=['GET'])
def get_all_platforms(platform_service: PlatformService = PlatformService()):
    """
    Get all platforms.

    This route retrieves a list of all available platforms.

    Authentication: Not required.

    Parameters:
    -----------
    platform_service : PlatformService, optional
        The platform service instance (default is a new instance of PlatformService).

    Returns:
    --------
    Response
        JSON response containing a list of all platforms.
    """
    platforms = platform_service.get_all()
    return jsonify(PlatformSchema(many=True).dump(platforms)), 200