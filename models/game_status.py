from app import db

class GameStatus(db.Model):
    __tablename__ = 'game_statuses'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    # Relationships
    user_reviews = db.relationship('UserReview', backref='game_status')
    
    def __repr__(self):
        return f'<Status {self.name}>'