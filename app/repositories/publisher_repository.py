from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.publisher import Publisher


class PublisherRepository:
    """
    Repository layer for Publisher model.

    This class provides methods to interact with the Publisher table in the database.
    It includes methods to create, retrieve, update, and delete publishers.

    Attributes:
    ----------
    db : SQLAlchemy
        The SQLAlchemy database instance.

    Methods:
    -------
    create(data: dict) -> Publisher:
        Creates a new publisher with the provided data.
    get(id: int) -> Publisher:
        Retrieves a publisher by its ID.
    get_all() -> list[Publisher]:
        Retrieves all publishers.
    update(publisher: Publisher, data: dict) -> Publisher:
        Updates an existing publisher with the provided data.
    delete(publisher: Publisher) -> None:
        Deletes the provided publisher.
    """

    def __init__(self, db: SQLAlchemy = db) -> None:
        """
        Initializes the PublisherRepository with the given SQLAlchemy database instance.

        Parameters:
        ----------
        db : SQLAlchemy, optional
            The SQLAlchemy database instance (default is the db instance from app).
        """
        self.db = db

    def create(self, data):
        """
        Create a new publisher.

        Parameters:
        ----------
        data : dict
            A dictionary containing the publisher data.

        Returns:
        -------
        Publisher
            The created Publisher object.
        """
        publisher = Publisher(**data)
        self.db.session.add(publisher)
        self.db.session.commit()
        return publisher
    
    def get(self, id):
        """
        Get a publisher by ID.

        Parameters:
        ----------
        id : int
            The ID of the publisher to retrieve.

        Returns:
        -------
        Publisher
            The Publisher object with the specified ID, or None if not found.
        """
        return Publisher.query.get(id)
    
    def get_all(self):
        """
        Get all publishers.

        Returns:
        -------
        list[Publisher]
            A list of all Publisher objects.
        """
        return Publisher.query.all()
    
    def update(self, publisher, data):
        """
        Update an existing publisher.

        Parameters:
        ----------
        publisher : Publisher
            The Publisher object to update.
        data : dict
            A dictionary containing the updated publisher data.

        Returns:
        -------
        Publisher
            The updated Publisher object.
        """
        for key, value in data.items():
            setattr(publisher, key, value)
        self.db.session.commit()
        return publisher
    
    def delete(self, publisher):
        """
        Delete a publisher.

        Parameters:
        ----------
        publisher : Publisher
            The Publisher object to delete.

        Returns:
        -------
        None
        """
        self.db.session.delete(publisher)
        self.db.session.commit()