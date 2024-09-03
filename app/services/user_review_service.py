from app.repositories.user_review_repository import UserReviewRepository

class UserReviewService:
    """
    Service layer for UserReview operations.

    This class provides methods to interact with the UserReviewRepository.
    It includes methods to retrieve a single user review by ID and to retrieve all user reviews.

    Attributes:
    ----------
    user_review_repository : UserReviewRepository
        The repository instance used to interact with the user review data.

    Methods:
    -------
    get(id: int) -> UserReview:
        Retrieves a user review by its ID.
    get_all() -> list[UserReview]:
        Retrieves all user reviews.
    """

    def __init__(self, user_review_repository: UserReviewRepository = UserReviewRepository()) -> None:
        """
        Initializes the UserReviewService with the given UserReviewRepository instance.

        Parameters:
        ----------
        user_review_repository : UserReviewRepository, optional
            The repository instance used to interact with the user review data (default is a new UserReviewRepository instance).
        """
        self.user_review_repository = user_review_repository

    def get(self, id):
        """
        Get a user review by ID.

        Parameters:
        ----------
        id : int
            The ID of the user review to retrieve.

        Returns:
        -------
        UserReview
            The UserReview object with the specified ID, or None if not found.
        """
        return self.user_review_repository.get(id)
    
    def get_all(self):
        """
        Get all user reviews.

        Returns:
        -------
        list[UserReview]
            A list of all UserReview objects.
        """
        return self.user_review_repository.get_all()
    
    def create(self, data):
        """
        Create a new user review.

        Parameters:
        ----------
        data : dict
            A dictionary containing the user review data.

        Returns:
        -------
        UserReview
            The created UserReview object.
        """

        # Check if user review already exists
        user_review = self.user_review_repository.get_by_user_and_game(data['user_id'], data['game_id'])

        if user_review:
            return {'message': 'User review already exists!'}
        

        return self.user_review_repository.create(data)
    
    def update(self, user_review, data):
        """
        Update a user review.

        Parameters:
        ----------
        id : int
            The ID of the user review to update.
        data : dict
            A dictionary containing the updated user review data.

        Returns:
        -------
        UserReview
            The updated UserReview object.
        """
        
        return self.user_review_repository.update(user_review, data)
    
    def delete(self, user_review):
        """
        Delete a user review.

        Parameters:
        ----------
        id : int
            The ID of the user review to delete.

        Returns:
        -------
        UserReview
            The deleted UserReview object.
        """
        
        return self.user_review_repository.delete(user_review)
    
    def get_by_user(self, user_id):
        """
        Get all user reviews by user.

        Parameters:
        ----------
        user_id : int
            The ID of the user.

        Returns:
        -------
        list[UserReview]
            A list of all UserReview objects by the specified user.
        """
        return self.user_review_repository.get_by_user(user_id)
    
    def get_by_game(self, game_id):
        """
        Get all user reviews by game.

        Parameters:
        ----------
        game_id : int
            The ID of the game.

        Returns:
        -------
        list[UserReview]
            A list of all UserReview objects by the specified game.
        """
        return self.user_review_repository.get_by_game(game_id)