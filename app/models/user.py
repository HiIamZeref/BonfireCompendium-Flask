from app import db
from app.models import Follower


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    bio = db.Column(db.String(255), nullable=True)
    photo = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    
    # Relationships
    user_reviews = db.relationship('UserReview', backref='user')
    user_gamelists = db.relationship('UserGameList')
    followed_users = db.relationship(
        'User',
        secondary='followers',
        primaryjoin=(id == Follower.follower_id),
        secondaryjoin=(id == Follower.user_id),
        backref='followers'
    )

