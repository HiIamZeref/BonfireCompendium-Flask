from app import db
from sqlalchemy import CheckConstraint

class UserReview(db.Model):
    __tablename__ = 'user_reviews'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    score = db.Column(db.Intege, CheckConstraint('score >= 1 AND score <= 10'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    mastered = db.Boolean(nullable=False, default=False)
    review = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    

    def __repr__(self):
        return f'<UserReview {self.id}>'