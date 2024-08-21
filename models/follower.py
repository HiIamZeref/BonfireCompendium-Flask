from app import db

class Follower(db.Model):
    __tablename__ = 'followers'

    # Columns
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    
    def __repr__(self):
        return f'<Follower {self.user_id} follows {self.follower_id}>'