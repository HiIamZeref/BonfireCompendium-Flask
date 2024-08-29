from app import db

class Genre(db.Model):
    __tablename__ = 'genres'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    # Relationships
    games = db.relationship('Game', backref='genre', lazy=True)
    
    def __repr__(self):
        return f'<Genre {self.name}>'