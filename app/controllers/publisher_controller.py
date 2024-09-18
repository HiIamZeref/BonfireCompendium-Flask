from flask import Blueprint, jsonify
from app.schemas.publisher_schema import PublisherSchema
from app.services.publisher_service import PublisherService

publishers = Blueprint('publishers', __name__)

# Publisher Controller Routes
@publishers.route('/<int:publisher_id>', methods=['GET'])
def get_publisher(publisher_id, publisher_service: PublisherService = PublisherService()):
    """Get a publisher by ID."""
    publisher = publisher_service.get(publisher_id)
    if not publisher:
        return jsonify({'message': 'Publisher not found'}), 404

    return jsonify(PublisherSchema().dump(publisher)), 200

@publishers.route('/', methods=['GET'])
def get_all_publishers(publisher_service: PublisherService = PublisherService()):
    """Get all publishers."""
    publishers = publisher_service.get_all()
    return jsonify(PublisherSchema(many=True).dump(publishers)), 200