from app import db

user_gamelist_has_game = db.Table(
    'user_gamelist_has_game',
    db.Column('gamelist_id', db.Integer, db.ForeignKey('gamelists.id'), primary_key=True),
    db.Column('game_id', db.Integer, db.ForeignKey('games.id'), primary_key=True)
)