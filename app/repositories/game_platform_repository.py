from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.game_platform import game_platform
from sqlalchemy import text

class GamePlatformRepository:
    '''
    Repository layer for GamePlatform model.

    This class provides methods to interact with the GamePlatform table in the database.
    It includes methods to create, retrieve, update, and delete game platforms.

    Attributes:
    ----------
    db : SQLAlchemy
        The SQLAlchemy database instance.

    Methods:
    -------
    create(data: dict) -> GamePlatform:
        Creates a new game platform with the provided data.
    get(id: int) -> GamePlatform:
        Retrieves a game platform by its ID.
    get_all() -> list[GamePlatform]:
        Retrieves all game platforms.
    update(game_platform: GamePlatform, data: dict) -> GamePlatform:
        Updates an existing game platform with the provided data.
    delete(game_platform: GamePlatform) -> GamePlatform:
        Deletes the provided game platform.
    '''

    def __init__(self, db: SQLAlchemy = db) -> None:
        '''
        Initializes the GamePlatformRepository with the given SQLAlchemy database instance.

        Parameters:
        ----------
        db : SQLAlchemy, optional
            The SQLAlchemy database instance (default is the db instance from app).
        '''
        self.db = db

    def create(self, data):
        '''
        Create a new game platform relation.

        Parameters:
        ----------
        data : dict
            A dictionary containing the game platform data.

        Returns:
        -------
        GamePlatform
            The created GamePlatform object.
        '''
        new_entry = game_platform.insert().values(data)
        self.db.session.execute(new_entry)
        self.db.session.commit()
        return game_platform
    
    def get(self, game_id, platform_id):
        '''
        Retrieve a game platform relation by its game and platform IDs.

        Parameters:
        ----------
        game_id : int
            The ID of the game to retrieve.
        platform_id : int
            The ID of the platform to retrieve.

        Returns:
        -------
        dict
            A dictionary representing the game platform relation, or None if not found.
        '''
        query = text(f'''
        SELECT * FROM game_platforms 
        WHERE game_id = :game_id AND platform_id = :platform_id
        ''')
        result = self.db.session.execute(query, {'game_id': game_id, 'platform_id': platform_id}).fetchone()
        return dict(result) if result else None

    def delete(self, game_id, platform_id):
        '''
        Delete a game platform relation by its game and platform IDs.

        Parameters:
        ----------
        game_id : int
            The ID of the game.
        platform_id : int
            The ID of the platform.
        '''
        query = game_platform.delete().where(
            game_platform.c.game_id == game_id and game_platform.c.platform_id == platform_id
        )
        self.db.session.execute(query)
        self.db.session.commit()

    def get_all_platforms(self, game_id):
        '''
        Retrieve all platforms for a given game.

        Parameters:
        ----------
        game_id : int
            The ID of the game to retrieve platforms for.

        Returns:
        -------
        list[dict]
            A list of platforms associated with the given game as dictionaries.
        '''
        query = text('''
        SELECT p.* FROM platforms p 
        JOIN game_platforms gp ON p.id = gp.platform_id 
        WHERE gp.game_id = :game_id
        ''')
        results = self.db.session.execute(query, {'game_id': game_id}).fetchall()
        return [dict(row) for row in results]
    
    def get_all_games(self, platform_id):
        '''
        Retrieve all games for a given platform.

        Parameters:
        ----------
        platform_id : int
            The ID of the platform to retrieve games for.

        Returns:
        -------
        list[dict]
            A list of games associated with the given platform as dictionaries.
        '''
        query = text('''
        SELECT g.* FROM games g 
        JOIN game_platforms gp ON g.id = gp.game_id 
        WHERE gp.platform_id = :platform_id
        ''')
        results = self.db.session.execute(query, {'platform_id': platform_id}).fetchall()
        return [dict(row) for row in results]
    
    