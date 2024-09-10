from app.repositories.game_repository import GameRepository

class GameService:
    """
    Service layer for Game operations.

    This class provides methods to interact with the GameRepository.
    It includes methods to create, retrieve, update, and delete games.

    Attributes:
    ----------
    game_repository : GameRepository
        The repository instance used to interact with the game data.

    Methods:
    -------
    create(data: dict) -> Game:
        Creates a new game.
    get(id: int) -> Game:
        Retrieves a game by its ID.
    get_all() -> list[Game]:
        Retrieves all games.
    update(game: Game, data: dict) -> Game:
        Updates a game.
    delete(game: Game) -> None:
        Deletes a game.
    get_by_title(title: str) -> Game:
        Retrieves a game by its title.
    """

    def __init__(self, game_repository: GameRepository = GameRepository()) -> None:
        """
        Initializes the GameService with the given GameRepository instance.

        Parameters:
        ----------
        game_repository : GameRepository, optional
            The repository instance used to interact with the game data (default is a new GameRepository instance).
        """
        self.game_repository = game_repository

    def create(self, data):
        """
        Create a new game.

        Parameters:
        ----------
        data : dict
            The data for the new game.

        Returns:
        -------
        Game
            The new Game object.
        """
        return self.game_repository.create(data)
    
    def get(self, id):
        """
        Get a game by ID.

        Parameters:
        ----------
        id : int
            The ID of the game to retrieve.

        Returns:
        -------
        Game
            The Game object with the specified ID, or None if not found.
        """
        return self.game_repository.get(id)
    
    def get_all(self):
        """
        Get all games.

        Returns:
        -------
        list[Game]
            A list of all Game objects.
        """
        return self.game_repository.get_all()
    
    def update(self, game, data):
        """
        Update a game.

        Parameters:
        ----------
        game : Game
            The game to update.
        data : dict
            The data to update the game with.

        Returns:
        -------
        Game
            The updated Game object.
        """
        return self.game_repository.update(game, data)
    
    def delete(self, game):
        """
        Delete a game.

        Parameters
        ----------
        game : Game
            The game to delete.
        """
        return self.game_repository.delete(game)
    
    def get_by_title(self, title):
        """
        Get a game by title.

        Parameters:
        ----------
        title : str
            The title of the game to retrieve.

        Returns:
        -------
        Game
            The Game object with the specified title, or None if not found.
        """
        return self.game_repository.get_by_title(title)