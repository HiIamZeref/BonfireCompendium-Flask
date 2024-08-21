from app import db

class Platform(db.Model):
    __tablename__ = 'platforms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    games = db.relationship('Game', backref='platform', lazy=True)
    
    def __repr__(self):
        return f'<Platform {self.name}>'