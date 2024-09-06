from flask_sqlalchemy import SQLAlchemy
from app.models.follower import Follower
from app import db

class FollowerRepository:
    '''
    Repository layer for Follower model.

    This class provides methods to interact with the Follower table in the database.
    It includes methods to create, retrieve, update, and delete followers.

    Attributes:
    ----------
    db : SQLAlchemy
        The SQLAlchemy database instance.

    Methods:
    -------
    get(user_id: int, follower_id: int) -> Follower:
        Retrieves a follower relationship.
    create(data: dict) -> Follower:
        Creates a new follower with the provided data.
    delete(follower: Follower) -> Follower:
        Deletes the provided follower.
    get_followers(user_id: int) -> list[Follower]:
        Retrieves all followers for a given user.
    get_following(follower_id: int) -> list[Follower]:
        Retrieves all users that a given user is following.
    '''

    def __init__(self, db: SQLAlchemy = db) -> None:
        '''
        Initializes the FollowerRepository with the given SQLAlchemy database instance.

        Parameters:
        ----------
        db : SQLAlchemy, optional
            The SQLAlchemy database instance (default is the db instance from app).
        '''
        self.db = db


    def get(self, user_id, follower_id):
        '''
        Get a follower relationship.

        Parameters:
        ----------
        user_id : int
            The ID of the user to retrieve the relationship for.
        follower_id : int
            The ID of the follower to retrieve the relationship for.

        Returns:
        -------
        Follower
            The Follower object.
        '''
        return Follower.query.filter_by(user_id=user_id, follower_id=follower_id).first()

    def create(self, data):
        '''
        Create a new follower.

        Parameters:
        ----------
        data : dict
            A dictionary containing the follower data.

        Returns:
        -------
        Follower
            The created Follower object.
        '''
        follower = Follower(**data)
        self.db.session.add(follower)
        self.db.session.commit()
        return follower

    
    def delete(self, relation):
        '''
        Delete a follower.

        Parameters:
        ----------
        follower : Follower
            The Follower object to delete.
        '''
        print(relation)
        relation = Follower.query.filter_by(user_id=relation.get('user_id'), follower_id=relation.get('follower_id')).first()

        if relation:
            self.db.session.delete(relation)
            self.db.session.commit()
        else:
            return 

    def get_followers(self, user_id):
        '''
        Get all followers for a given user.

        Parameters:
        ----------
        user_id : int
            The ID of the user to retrieve followers for.

        Returns:
        -------
        list[Follower]
            A list of all followers for the specified user.
        '''
        return Follower.query.filter_by(user_id=user_id).all()
    
    def get_following(self, follower_id):
        '''
        Get all users that a given user is following.

        Parameters:
        ----------
        follower_id : int
            The ID of the user who is following.

        Returns:
        -------
        list[Follower]
            A list of all users that the specified user is following.
        '''
        return Follower.query.filter_by(follower_id=follower_id).all()