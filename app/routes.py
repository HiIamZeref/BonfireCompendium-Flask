from flask import Blueprint
from app.controllers.user_controller import users

# Main blueprint
api = Blueprint('api', __name__)

# Registering blueprints
api.register_blueprint(users, url_prefix='/users')