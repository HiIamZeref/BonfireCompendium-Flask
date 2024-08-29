from app import db
from app.models.user_gamelist_has_game import user_gamelist_has_game

class UserGameList(db.Model):
    __tablename__ = 'user_gamelists'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships
    user = db.relationship('User', lazy=True)
    games = db.relationship('Game', secondary=user_gamelist_has_game)

    def __repr__(self):
        return f'<UserGameList {self.user_id}>'