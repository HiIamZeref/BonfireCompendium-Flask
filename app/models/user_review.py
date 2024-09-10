from app import db
from sqlalchemy import CheckConstraint
from flask_sqlalchemy import SQLAlchemy


class UserReview(db.Model):
    __tablename__ = 'user_reviews'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    score = db.Column(db.Integer, CheckConstraint('score >= 1 AND score <= 10'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('game_statuses.id'), nullable=False)
    mastered = db.Boolean()
    review = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Relationships
    game = db.relationship('Game',foreign_keys=[game_id], backref='user_reviews')
    user = db.relationship('User', foreign_keys=[user_id], backref='user_reviews')
    status = db.relationship('GameStatus', foreign_keys=[status_id], backref='user_reviews')


   
    def __repr__(self):
        return f'<UserReview {self.id}>'