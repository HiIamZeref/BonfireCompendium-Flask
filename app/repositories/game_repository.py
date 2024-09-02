from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.game import Game

class GameRepository:
    '''
    Repository layer for Game model.
    '''
    def __init__(self, db = db) -> None:
        self.db = db

    def create(self, data):
        '''
        Create a new game.
        '''
        game = Game(**data)
        self.db.session.add(game)
        self.db.session.commit()
        return game
    
    def get(self, id):
        '''
        Get a game by ID.
        '''
        return Game.query.get(id)
    
    def get_all(self):
        '''
        Get all games.
        '''
        return Game.query.all()
    
    def update(self, game, data):
        '''
        Update a game.
        '''
        for key, value in data.items():
            setattr(game, key, value)
        
        self.db.session.commit()
        return game
    
    def delete(self, game):
        '''
        Delete a game.
        '''
        self.db.session.delete(game)
        self.db.session.commit()
        return game
    
    def get_by_title(self, title):
        '''
        Get a game by title.
        '''
        return Game.query.filter_by(title=title).first()
        