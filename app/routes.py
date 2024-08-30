from flask import Blueprint
from app.controllers.developer_controller import developers
from app.controllers.user_controller import users


# Main blueprint
api = Blueprint('api', __name__)

# Registering blueprints
api.register_blueprint(developers, url_prefix='/developers')
api.register_blueprint(users, url_prefix='/users')