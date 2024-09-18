from flask import Blueprint
from app.controllers.auth_controller import auth
from app.controllers.developer_controller import developers
from app.controllers.follower_controller import followers
from app.controllers.game_controller import games
from app.controllers.game_status_controller import game_statuses
from app.controllers.game_platform_controller import game_platforms
from app.controllers.genre_controller import genres
from app.controllers.platform_controller import platforms
from app.controllers.publisher_controller import publishers
from app.controllers.user_controller import users
from app.controllers.user_backlog_controller import user_backlogs
from app.controllers.user_review_controller import user_reviews


# Main blueprint
api = Blueprint('api', __name__)

# Registering blueprints
api.register_blueprint(auth, url_prefix='/auth')
api.register_blueprint(developers, url_prefix='/developers')
api.register_blueprint(followers, url_prefix='/followers')
api.register_blueprint(games, url_prefix='/games')
api.register_blueprint(game_statuses, url_prefix='/game_statuses')
api.register_blueprint(game_platforms, url_prefix='/game_platforms')
api.register_blueprint(genres, url_prefix='/genres')
api.register_blueprint(platforms, url_prefix='/platforms')
api.register_blueprint(publishers, url_prefix='/publishers')
api.register_blueprint(users, url_prefix='/users')
api.register_blueprint(user_backlogs, url_prefix='/user_backlogs')
api.register_blueprint(user_reviews, url_prefix='/user_reviews')