from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.game_platform import GamePlatform

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
        Create a new game platform.

        Parameters:
        ----------
        data : dict
            A dictionary containing the game platform data.

        Returns:
        -------
        GamePlatform
            The created GamePlatform object.
        '''
        game_platform = GamePlatform(**data)
        self.db.session.add(game_platform)
        self.db.session.commit()
        return game_platform
    
    def get(self, id):
        '''
        Retrieve a game platform by its ID.

        Parameters:
        ----------
        id : int
            The ID of the game platform to retrieve.

        Returns:
        -------
        GamePlatform
            The GamePlatform object with the provided ID, or None if not found.
        '''
        return GamePlatform.query.get(id)

    def get_all(self):
        '''
        Retrieve all game platforms.

        Returns:
        -------
        list[GamePlatform]
            A list of all GamePlatform objects in the database.
        '''
        return GamePlatform.query.all()

    def update(self, game_platform, data):
        '''
        Update an existing game platform with the provided data.

        Parameters:
        ----------
        game_platform : GamePlatform
            The GamePlatform object to update.
        data : dict
            A dictionary containing the new game platform data.

        Returns:
        -------
        GamePlatform
            The updated GamePlatform object.
        '''
        for key, value in data.items():
            setattr(game_platform, key, value)
        self.db.session.commit()
        return game_platform
    
    