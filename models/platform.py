from app import db
from models.game_platform import game_platform

class Platform(db.Model):
    __tablename__ = 'platforms'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    # Relationships
    games = db.relationship('Game', secondary=game_platform, backref='platforms')
    
    def __repr__(self):
        return f'<Platform {self.name}>'