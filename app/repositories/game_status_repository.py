from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.game_status import GameStatus

class GameStatusRepository:
    '''
    Repository layer for GameStatus model.

    This class provides methods to interact with the GameStatus table in the database.
    It includes methods to create, retrieve, update, and delete game statuses.

    Attributes:
    ----------
    db : SQLAlchemy
        The SQLAlchemy database instance.

    Methods:
    -------
    create(data: dict) -> GameStatus:
        Creates a new game status with the provided data.
    get(id: int) -> GameStatus:
        Retrieves a game status by its ID.
    get_all() -> list[GameStatus]:
        Retrieves all game statuses.
    update(game_status: GameStatus, data: dict) -> GameStatus:
        Updates an existing game status with the provided data.
    delete(game_status: GameStatus) -> GameStatus:
        Deletes the provided game status.
    '''

    def __init__(self, db: SQLAlchemy = db) -> None:
        '''
        Initializes the GameStatusRepository with the given SQLAlchemy database instance.

        Parameters:
        ----------
        db : SQLAlchemy, optional
            The SQLAlchemy database instance (default is the db instance from app).
        '''
        self.db = db

    def create(self, data):
        '''
        Create a new game status.

        Parameters:
        ----------
        data : dict
            A dictionary containing the game status data.

        Returns:
        -------
        GameStatus
            The created GameStatus object.
        '''
        game_status = GameStatus(**data)
        self.db.session.add(game_status)
        self.db.session.commit()
        return game_status
    
    def get(self, id):
        '''
        Retrieve a game status by its ID.

        Parameters:
        ----------
        id : int
            The ID of the game status to retrieve.

        Returns:
        -------
        GameStatus
            The GameStatus object with the provided ID.
        '''
        return GameStatus.query.get(id)

    def get_all(self):
        '''
        Retrieve all game statuses.

        Returns:
        -------
        list[GameStatus]
            A list of all GameStatus objects in the database.
        '''
        return GameStatus.query.all()

    def update(self, game_status, data):
        '''
        Update an existing game status with the provided data.

        Parameters:
        ----------
        game_status : GameStatus
            The GameStatus object to update.
        data : dict
            A dictionary containing the updated game status data.

        Returns:
        -------
        GameStatus
            The updated GameStatus object.
        '''
        for key, value in data.items():
            setattr(game_status, key, value)
        self.db.session.commit()
        return game_status
    
    def delete(self, game_status):
        '''
        Delete the provided game status.

        Parameters:
        ----------
        game_status : GameStatus
            The GameStatus object to delete.

        Returns:
        -------
        GameStatus
            The deleted GameStatus object.
        '''
        self.db.session.delete(game_status)
        self.db.session.commit()
        return game_status