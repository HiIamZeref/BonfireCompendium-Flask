from app import db

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
    genre = db.relationship('Genre', foreign_keys=[genre_id], backref='games')
    developer = db.relationship('Developer', foreign_keys=[developer_id], backref='games')
    publisher = db.relationship('Publisher', foreign_keys=[publisher_id], backref='games')
    
    def __repr__(self):
        return f'<Game {self.title}>'