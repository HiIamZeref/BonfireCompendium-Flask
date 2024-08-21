from app import db

game_platform = db.Table(
    'game_platforms',
    db.Column('game_id', db.Integer, db.ForeignKey('games.id'), primary_key=True),
    db.Column('platform_id', db.Integer, db.ForeignKey('platforms.id'), primary_key=True)
)