from app import db
from app.models.game_platform import game_platform
from app.models.user_gamelist_has_game import user_gamelist_has_game

class Game(db.Model):
    """
    Game model representing a video game in the database.

    Attributes:
    ----------
    id : int
        Primary key, unique identifier for the game.
    title : str
        Title of the game, must be unique and not null.
    description : str
        Description of the game, not null.
    release_date : date
        Release date of the game, not null.
    genre_id : int
        Foreign key referencing the genres table, not null.
    developer_id : int
        Foreign key referencing the developers table, not null.
    publisher_id : int
        Foreign key referencing the publishers table, not null.
    cover_image : str
        URL or path to the cover image of the game, can be null.

    Relationships:
    -------------
    platforms : list of Platform
        Many-to-many relationship with the platforms table.
    user_gamelist : list of UserGameList
        Many-to-many relationship with the user_gamelist_has_game table.
    user_reviews : list of UserReview
        One-to-many relationship with the user_reviews table.

    Methods:
    -------
    __repr__():
        Returns a string representation of the Game instance.
    """
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