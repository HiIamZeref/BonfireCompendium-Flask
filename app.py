from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import (
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
    User
)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True, port=5000)