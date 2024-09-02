from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.genre import Genre

class GenreRepository:
    '''
    Repository layer for Genre model.

    This class provides methods to interact with the Genre table in the database.
    It includes methods to create, retrieve, update, and delete genres.

    Attributes:
    ----------
    db : SQLAlchemy
        The SQLAlchemy database instance.

    Methods:
    -------
    create(data: dict) -> Genre:
        Creates a new genre with the provided data.
    get(id: int) -> Genre:
        Retrieves a genre by its ID.
    get_all() -> list[Genre]:
        Retrieves all genres.
    update(genre: Genre, data: dict) -> Genre:
        Updates an existing genre with the provided data.
    delete(genre: Genre) -> Genre:
        Deletes the provided genre.
    '''

    def __init__(self, db: SQLAlchemy = db) -> None:
        '''
        Initializes the GenreRepository with the given SQLAlchemy database instance.

        Parameters:
        ----------
        db : SQLAlchemy, optional
            The SQLAlchemy database instance (default is the db instance from app).
        '''
        self.db = db

    def create(self, data):
        '''
        Create a new genre.

        Parameters:
        ----------
        data : dict
            A dictionary containing the genre data.

        Returns:
        -------
        Genre
            The created Genre object.
        '''
        genre = Genre(**data)
        self.db.session.add(genre)
        self.db.session.commit()
        return genre
    
    def get(self, id):
        '''
        Get a genre by ID.

        Parameters:
        ----------
        id : int
            The ID of the genre to retrieve.

        Returns:
        -------
        Genre
            The Genre object with the specified ID, or None if not found.
        '''
        return Genre.query.get(id)
    
    def get_all(self):
        '''
        Get all genres.

        Returns:
        -------
        list[Genre]
            A list of all Genre objects.
        '''
        return Genre.query.all()
    
    def update(self, genre, data):
        '''
        Update an existing genre.

        Parameters:
        ----------
        genre : Genre
            The Genre object to update.
        data : dict
            A dictionary containing the updated genre data.

        Returns:
        -------
        Genre
            The updated Genre object.
        '''
        for key, value in data.items():
            setattr(genre, key, value)
        
        self.db.session.commit()
        return genre
    
    def delete(self, genre):
        '''
        Delete a genre.

        Parameters:
        ----------
        genre : Genre
            The Genre object to delete.

        Returns:
        -------
        Genre
            The deleted Genre object.
        '''
        self.db.session.delete(genre)
        self.db.session.commit()
        return genre
        