from app.repositories.user_backlog_repository import UserBacklogRepository

class UserBacklogService:
    """
    Service layer for UserBacklog operations.

    This class provides methods to interact with the UserBacklogRepository.
    It includes methods to create, delete, and retrieve user backlog entries.

    Attributes:
    ----------
    user_backlog_repository : UserBacklogRepository
        The repository instance used to interact with the user backlog data.

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
    """
    
    def __init__(self,
                 user_backlog_repository: UserBacklogRepository= UserBacklogRepository()):
        '''
        Initializes the UserBacklogService with the given UserBacklogRepository.

        Parameters:
        ----------
        user_backlog_repository : UserBacklogRepository, optional
            The UserBacklogRepository instance (default is the UserBacklogRepository instance from app).
        '''
        self.user_backlog_repository = user_backlog_repository

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
        return self.user_backlog_repository.get(user_id, game_id)

    def create(self, data):
        '''
        Create a new user backlog entry.
        '''
        return self.user_backlog_repository.create(data)

    def delete(self, user_backlog):
        '''
        Delete a user backlog entry.
        '''
        return self.user_backlog_repository.delete(user_backlog)

    def get_backlog(self, user_id):
        '''
        Get all games in a user's backlog.
        '''
        return self.user_backlog_repository.get_backlog(user_id)