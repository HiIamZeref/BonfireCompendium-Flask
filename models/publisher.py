from app import db

class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    games = db.relationship('Game', backref='publisher', lazy=True)
    
    def __repr__(self):
        return f'<Publisher {self.name}>'