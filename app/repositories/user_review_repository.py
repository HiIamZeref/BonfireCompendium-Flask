from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.user_review import UserReview

class UserReviewRepository:
    '''
    Repository layer for UserReview model.

    This class provides methods to interact with the UserReview table in the database.
    It includes methods to create, retrieve, update, and delete user reviews.

    Attributes:
    ----------
    db : SQLAlchemy
        The SQLAlchemy database instance.

    Methods:
    -------
    create(data: dict) -> UserReview:
        Creates a new user review with the provided data.
    get(id: int) -> UserReview:
        Retrieves a user review by its ID.
    get_all() -> list[UserReview]:
        Retrieves all user reviews.
    update(user_review: UserReview, data: dict) -> UserReview:
        Updates an existing user review with the provided data.
    delete(user_review: UserReview) -> UserReview:
        Deletes the provided user review.
    '''

    def __init__(self, db: SQLAlchemy = db) -> None:
        '''
        Initializes the UserReviewRepository with the given SQLAlchemy database instance.

        Parameters:
        ----------
        db : SQLAlchemy, optional
            The SQLAlchemy database instance (default is the db instance from app).
        '''
        self.db = db

    def create(self, data):
        '''
        Create a new user review.

        Parameters:
        ----------
        data : dict
            A dictionary containing the user review data.

        Returns:
        -------
        UserReview
            The created UserReview object.
        '''
        user_review = UserReview(**data)
        self.db.session.add(user_review)
        self.db.session.commit()
        return user_review
    
    def get(self, id):
        '''
        Retrieve a user review by its ID.

        Parameters:
        ----------
        id : int
            The ID of the user review to retrieve.

        Returns:
        -------
        UserReview
            The UserReview object with the provided ID.
        '''
        return UserReview.query.get(id)

    def get_all(self):
        '''
        Retrieve all user reviews.

        Returns:
        -------
        list[UserReview]
            A list of all UserReview objects in the database.
        '''
        return UserReview.query.all()

    def update(self, user_review, data):
        '''
        Update an existing user review with the provided data.

        Parameters:
        ----------
        user_review : UserReview
            The user review to update.
        data : dict
            A dictionary containing the updated user review data.

        Returns:
        -------
        UserReview
            The updated UserReview object.
        '''
        for key, value in data.items():
            setattr(user_review, key, value)
        self.db.session.commit()
        return user_review
    
    def delete(self, user_review):
        '''
        Delete a user review.

        Parameters:
        ----------
        user_review : UserReview
            The user review to delete.
        '''
        self.db.session.delete(user_review)
        self.db.session.commit()
        return user_review
    
    def get_by_user_id(self, user_id):
        '''
        Retrieve all user reviews by user ID.

        Parameters:
        ----------
        user_id : int
            The ID of the user whose reviews to retrieve.

        Returns:
        -------
        list[UserReview]
            A list of all UserReview objects for the specified user.
        '''
        return UserReview.query.filter_by(user_id=user_id).all()
    
    def get_by_game_id(self, game_id):
        '''
        Retrieve all user reviews by game ID.

        Parameters:
        ----------
        game_id : int
            The ID of the game whose reviews to retrieve.

        Returns:
        -------
        list[UserReview]
            A list of all UserReview objects for the specified game.
        '''
        return UserReview.query.filter_by(game_id=game_id).all()
    
    def get_by_user_game_id(self, user_id, game_id):
        '''
        Retrieve a user review by user ID and game ID.

        Parameters:
        ----------
        user_id : int
            The ID of the user who wrote the review.
        game_id : int
            The ID of the game being reviewed.

        Returns:
        -------
        UserReview
            The UserReview object with the specified user and game IDs.
        '''
        return UserReview.query.filter_by(user_id=user_id, game_id=game_id).first()
    
