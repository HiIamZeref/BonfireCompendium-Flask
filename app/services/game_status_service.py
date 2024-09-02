from app.repositories.game_status_repository import GameStatusRepository

class GameStatusService:
    """
    Service layer for GameStatus operations.

    This class provides methods to interact with the GameStatusRepository.
    It includes methods to retrieve a single game status by ID and to retrieve all game statuses.

    Attributes:
    ----------
    game_status_repository : GameStatusRepository
        The repository instance used to interact with the game status data.

    Methods:
    -------
    get(id: int) -> GameStatus:
        Retrieves a game status by its ID.
    get_all() -> list[GameStatus]:
        Retrieves all game statuses.
    """

    def __init__(self, game_status_repository: GameStatusRepository = GameStatusRepository()) -> None:
        """
        Initializes the GameStatusService with the given GameStatusRepository instance.

        Parameters:
        ----------
        game_status_repository : GameStatusRepository, optional
            The repository instance used to interact with the game status data (default is a new GameStatusRepository instance).
        """
        self.game_status_repository = game_status_repository

    def get(self, id):
        """
        Get a game status by ID.

        Parameters:
        ----------
        id : int
            The ID of the game status to retrieve.

        Returns:
        -------
        GameStatus
            The GameStatus object with the specified ID, or None if not found.
        """
        return self.game_status_repository.get(id)
    
    def get_all(self):
        """
        Get all game statuses.

        Returns:
        -------
        list[GameStatus]
            A list of all GameStatus objects.
        """
        return self.game_status_repository.get_all()