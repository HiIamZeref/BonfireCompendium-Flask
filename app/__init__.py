from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from app.config.config import Config
import os
from datetime import timedelta


# Load environment variables
load_dotenv()

# Create the Flask application instance
app = Flask(__name__)

# Creating config file
config = Config().dev_config

# Using dev env
app.env = config.ENV

# Update configuration for the database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

# Update configuration for JWT
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

# Initialize Flask extensions using the container
db = SQLAlchemy(app)

# Initialize Flask-Bcrypt
bcrypt = Bcrypt(app)

# Initialize Flask-JWT-Extended
jwt = JWTManager(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import models so they are registered with SQLAlchemy
from app.models import (
    Developer,
    Follower,
    game_platform,
    GameStatus,
    Game,
    Genre,
    Platform,
    Publisher,
    user_gamelist_has_game,
    UserGameList,
    UserReview,
    User,
    UserBacklog
)

# Register commands
from app.commands.seed import register_seed_commands
register_seed_commands(app)


# Register routes
from app.routes import api
app.register_blueprint(api, url_prefix='/api/v1')


