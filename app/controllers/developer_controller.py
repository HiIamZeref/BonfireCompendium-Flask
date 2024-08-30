from flask import Blueprint, request, jsonify
from app.schemas.developer_schema import DeveloperSchema
from app.services.developer_service import DeveloperService

# Blueprint for developers  
developers = Blueprint('developers', __name__)

# Developer Controller Routes
def get_developer(developer_id, developer_service: DeveloperService = DeveloperService()):
    """Get a developer by ID."""
    developer = developer_service.get(developer_id)
    if not developer:
        return jsonify({'message': 'Developer not found'}), 404

    return jsonify(DeveloperSchema().dump(developer)), 200

def get_all_developers(developer_service: DeveloperService = DeveloperService()):
    """Get all developers."""
    developers = developer_service.get_all()
    return jsonify(DeveloperSchema(many=True).dump(developers)), 200