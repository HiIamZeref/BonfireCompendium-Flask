from flask_sqlalchemy import SQLAlchemy
from app.models.user_backlog import UserBacklog
from app import db

class UserBacklogRepository:
    '''
    Repository layer for UserBacklog model.

    This class provides methods to interact with the UserBacklog table in the database.
    It includes methods to create, retrieve, update, and delete user backlogs.

    Attributes:
    ----------
    db : SQLAlchemy
        The SQLAlchemy database instance.

    Methods:
    -------
    get(user_id: int, game_id: int) -> UserBacklog:
        Retrieves a user backlog entry.
    create(data: dict) -> UserBacklog:
        Creates a new user backlog entry with the provided data.
    delete(user_backlog: UserBacklog) -> UserBacklog:
        Deletes the provided user backlog entry.
    get_backlog(user_id: int) -> list[UserBacklog]:
        Retrieves all games in a user's backlog.
    '''
    def __init__(self, db: SQLAlchemy = db) -> None:
        '''
        Initializes the UserBacklogRepository with the given SQLAlchemy database instance.

        Parameters:
        ----------
        db : SQLAlchemy, optional
            The SQLAlchemy database instance (default is the db instance from app).
        '''
        self.db = db

    def get(self, user_id, game_id):
        '''
        Get a user backlog entry.

        Parameters:
        ----------
        user_id : int
            The ID of the user to retrieve the backlog entry for.
        game_id : int
            The ID of the game to retrieve the backlog entry for.

        Returns:
        -------
        UserBacklog
            The UserBacklog object.
        '''
        return UserBacklog.query.filter_by(user_id=user_id, game_id=game_id).first()

    def create(self, data):
        '''
        Create a new user backlog entry.
        '''
        user_backlog = UserBacklog(**data)
        self.db.session.add(user_backlog)
        self.db.session.commit()
        return user_backlog

    def delete(self, user_backlog):
        '''
        Delete a user backlog entry.
        '''
        self.db.session.delete(user_backlog)
        self.db.session.commit()
        return user_backlog

    def get_backlog(self, user_id):
        '''
        Get all games in a user's backlog.
        '''
        return UserBacklog.query.filter_by(user_id=user_id).all()