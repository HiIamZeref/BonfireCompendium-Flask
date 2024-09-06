from app import db

class Follower(db.Model):
    __tablename__ = 'followers'

    # Columns
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

    # Relationships
    user = db.relationship('User', foreign_keys=[user_id], backref='user_followers')
    follower = db.relationship('User', foreign_keys=[follower_id], backref='user_following')
    
    def __repr__(self):
        return f'<Follower {self.user_id} follows {self.follower_id}>'