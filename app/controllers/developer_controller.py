from flask import Blueprint, request, jsonify
from app.schemas.developer_schema import DeveloperSchema
from app.services.developer_service import DeveloperService

"""
Developer Controller

This module defines the routes and request handlers for developer-related operations.
It uses Flask's Blueprint to organize the routes and Marshmallow for data validation and serialization.

Routes:
-------
GET /developers/<int:developer_id>:
    Get a developer by ID.
    - Path Parameters:
        - developer_id (int): The ID of the developer to retrieve.
    - Responses:
        - 200: Developer details returned successfully.
        - 404: Developer not found.

GET /developers/:
    Get a list of all developers.
    - Responses:
        - 200: List of all developers returned successfully.

Attributes:
-----------
developers : Blueprint
    The Blueprint instance for developer routes.
"""

# Blueprint for developers  
developers = Blueprint('developers', __name__)

# Developer Controller Routes
@developers.route('/<int:developer_id>', methods=['GET'])
def get_developer(developer_id, developer_service: DeveloperService = DeveloperService()):
    """
    Get a developer by ID.

    This route retrieves the details of a developer using the provided developer ID.

    Parameters:
    -----------
    developer_id : int
        The ID of the developer to retrieve.
    developer_service : DeveloperService, optional
        The developer service instance (default is a new instance of DeveloperService).

    Returns:
    --------
    Response
        JSON response containing the developer details if found, or an error message if the developer is not found.
    """
    developer = developer_service.get(developer_id)
    if not developer:
        return jsonify({'message': 'Developer not found'}), 404

    return jsonify(DeveloperSchema().dump(developer)), 200

@developers.route('/', methods=['GET'])
def get_all_developers(developer_service: DeveloperService = DeveloperService()):
    """
    Get all developers.

    This route retrieves a list of all developers.

    Parameters:
    -----------
    developer_service : DeveloperService, optional
        The developer service instance (default is a new instance of DeveloperService).

    Returns:
    --------
    Response
        JSON response containing a list of all developers.
    """
    developers = developer_service.get_all()
    return jsonify(DeveloperSchema(many=True).dump(developers)), 200
