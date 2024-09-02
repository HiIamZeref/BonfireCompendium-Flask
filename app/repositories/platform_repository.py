from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.platform import Platform

class PlatformRepository:
    '''
    Repository layer for Platform model.

    This class provides methods to interact with the Platform table in the database.
    It includes methods to create, retrieve, update, and delete platforms.

    Attributes:
    ----------
    db : SQLAlchemy
        The SQLAlchemy database instance.

    Methods:
    -------
    create(data: dict) -> Platform:
        Creates a new platform with the provided data.
    get(id: int) -> Platform:
        Retrieves a platform by its ID.
    get_all() -> list[Platform]:
        Retrieves all platforms.
    update(platform: Platform, data: dict) -> Platform:
        Updates an existing platform with the provided data.
    delete(platform: Platform) -> Platform:
        Deletes the provided platform.
    '''

    def __init__(self, db: SQLAlchemy = db) -> None:
        '''
        Initializes the PlatformRepository with the given SQLAlchemy database instance.

        Parameters:
        ----------
        db : SQLAlchemy, optional
            The SQLAlchemy database instance (default is the db instance from app).
        '''
        self.db = db

    def create(self, data):
        '''
        Create a new platform.

        Parameters:
        ----------
        data : dict
            A dictionary containing the platform data.

        Returns:
        -------
        Platform
            The created Platform object.
        '''
        platform = Platform(**data)
        self.db.session.add(platform)
        self.db.session.commit()
        return platform

    def get(self, id):
        '''
        Retrieve a platform by its ID.

        Parameters:
        ----------
        id : int
            The ID of the platform to retrieve.

        Returns:
        -------
        Platform
            The Platform object with the specified ID, or None if not found.
        '''
        return Platform.query.get(id)

    def get_all(self):
        '''
        Retrieve all platforms.

        Returns:
        -------
        list[Platform]
            A list of all Platform objects in the database.
        '''
        return Platform.query.all()

    def update(self, platform, data):
        '''
        Update an existing platform with the provided data.

        Parameters:
        ----------
        platform : Platform
            The Platform object to update.
        data : dict
            A dictionary containing the new platform data.

        Returns:
        -------
        Platform
            The updated Platform object.
        '''
        for key, value in data.items():
            setattr(platform, key, value)
        self.db.session.commit()
        return platform

    def delete(self, platform):
        '''
        Delete the provided platform.

        Parameters:
        ----------
        platform : Platform
            The Platform object to delete.

        Returns:
        -------
        Platform
            The deleted Platform object.
        '''
        self.db.session.delete(platform)
        self.db.session.commit()
        return platform