# Main imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_injector import FlaskInjector

# App Config
app = Flask(__name__)

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


bcrypt = Bcrypt(app)

# Migrate Config
from models import *
migrate = Migrate(app, db)

# Repositories import
# from repositories import (
#     UserRepository
# )
# # Services import
# from services import (
#     UserService
# )
# # Blueprints import 
# from controllers import (
#     UserController
# )


# Flask Injector Config
# def configure(binder):
#     # Repositories
#     binder.bind(UserRepository, to=UserRepository)

#     # Services
#     binder.bind(UserService, to=UserService)

# FlaskInjector(app=app, modules=[configure])

# Bcrypt Config

# Blueprints
# blueprints = [
#     UserController.user_blueprint
# ]

# for blueprint in blueprints:
#     app.register_blueprint(blueprint, url_prefix='/api/v1')


if __name__ == '__main__':
    app.run(debug=True, port=5000)