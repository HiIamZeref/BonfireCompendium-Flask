from app import db


class UserBacklog(db.Model):
    __tablename__ = 'user_backlogs'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships
    game = db.relationship('Game', foreign_keys=[game_id], backref='user_backlogs')
    user = db.relationship('User', foreign_keys=[user_id], backref='user_backlogs')

    def __repr__(self):
        return f'<UserBacklog {self.id}>'