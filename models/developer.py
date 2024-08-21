from app import db

class Developer(db.Model):
    __tablename__ = 'developers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    games = db.relationship('Game', backref='developer', lazy=True)