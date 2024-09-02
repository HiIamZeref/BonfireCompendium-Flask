from flask import Blueprint
from app.controllers.developer_controller import developers
from app.controllers.genre_controller import genres
from app.controllers.platform_controller import platforms
from app.controllers.publisher_controller import publishers
from app.controllers.user_controller import users


# Main blueprint
api = Blueprint('api', __name__)

# Registering blueprints
api.register_blueprint(developers, url_prefix='/developers')
api.register_blueprint(genres, url_prefix='/genres')
api.register_blueprint(platforms, url_prefix='/platforms')
api.register_blueprint(publishers, url_prefix='/publishers')
api.register_blueprint(users, url_prefix='/users')