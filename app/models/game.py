from app import db
from app.models.game_platform import game_platform
from app.models.user_gamelist_has_game import user_gamelist_has_game

class Game(db.Model):
    __tablename__ = 'games'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    cover_image = db.Column(db.String(255), nullable=True)

    # Relationships
    platforms = db.relationship('Platform', secondary=game_platform)
    user_gamelist = db.relationship('UserGameList', secondary=user_gamelist_has_game)
    user_reviews = db.relationship('UserReview', backref='game')
    
    def __repr__(self):
        return f'<Game {self.title}>'