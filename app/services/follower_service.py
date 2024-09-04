from app.repositories.follower_repository import FollowerRepository
from app.repositories.user_repository import UserRepository

class FollowerService:
    """
    Service layer for Follower operations.

    This class provides methods to interact with the FollowerRepository.
    It includes methods to follow and unfollow users.

    Attributes:
    ----------
    follower_repository : FollowerRepository
        The repository instance used to interact with the follower data.

    Methods:
    -------
    follow(data: dict) -> Follower:
        Follows a user by creating a new follower entry.
    unfollow(follower: Follower) -> None:
        Unfollows a user by deleting the follower entry.
    get_followers(user_id: int) -> list[Follower]:
        Retrieves all followers for a given user.
    get_following(follower_id: int) -> list[Follower]:
        Retrieves all users that a given user is following.
    """
    
    def __init__(self,
                 follower_repository: FollowerRepository= FollowerRepository(),
                 user_repository: UserRepository = UserRepository()):
        '''
        Initializes the FollowerService with the given FollowerRepository.

        Parameters:
        ----------
        follower_repository : FollowerRepository, optional
            The FollowerRepository instance (default is the FollowerRepository instance from app).
        user_repository : UserRepository, optional
            The UserRepository instance (default is the UserRepository instance from app).
        '''
        self.follower_repository = follower_repository
        self.user_repository = user_repository

    def follow(self, data):
        '''
        Follow a user.

        Parameters:
        ----------
        data : dict
            A dictionary containing the follower data.

        Returns:
        -------
        Follower
            The created Follower object.
        '''
        # Check if user exits
        user = self.user_repository.get(data['user_id'])
        if not user:
            raise ValueError('User not found')
        
        
        return self.follower_repository.create(data)
    
    def unfollow(self, follower):
        '''
        Unfollow a user.

        Parameters:
        ----------
        follower : Follower
            The Follower object to delete.
        '''
        self.follower_repository.delete(follower)

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
            A list of Follower objects.
        '''
        return self.follower_repository.get_followers(user_id)
    
    def get_following(self, follower_id):
        '''
        Get all users that a given user is following.

        Parameters:
        ----------
        follower_id : int
            The ID of the user to retrieve following for.

        Returns:
        -------
        list[Follower]
            A list of Follower objects.
        '''
        return self.follower_repository.get_following(follower_id)

    