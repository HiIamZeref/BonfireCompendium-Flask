from app.repositories.game_platform_repository import GamePlatformRepository

class GamePlatformService:
    """
    Service class for managing game-platform relationships.

    This class provides methods to create, delete, and retrieve game-platform relationships.
    It interacts with the GamePlatformRepository to perform database operations.

    Methods:
    --------
    __init__():
        Initializes the GamePlatformService with a GamePlatformRepository instance.

    create_game_platform(game_id: int, platform_id: int) -> dict:
        Creates a new game-platform relationship.
        - Parameters:
            - game_id (int): The ID of the game.
            - platform_id (int): The ID of the platform.
        - Returns:
            - dict: A message indicating whether the game-platform relationship was created or already exists.

    delete_game_platform(game_id: int, platform_id: int) -> bool:
        Deletes a game-platform relationship.
        - Parameters:
            - game_id (int): The ID of the game.
            - platform_id (int): The ID of the platform.
        - Returns:
            - bool: True if the relationship was deleted, False otherwise.

    get_platform_by_game(game_id: int) -> list:
        Retrieves all platforms associated with a given game.
        - Parameters:
            - game_id (int): The ID of the game.
        - Returns:
            - list: A list of platforms associated with the game.

    get_game_by_platform(platform_id: int) -> list:
        Retrieves all games associated with a given platform.
        - Parameters:
            - platform_id (int): The ID of the platform.
        - Returns:
            - list: A list of games associated with the platform.
    """
        
    def __init__(self):
        self.game_platform_repository = GamePlatformRepository()

    def create_game_platform(self, game_id, platform_id):
        # Check if game platform already exists
        game_platform = self.game_platform_repository.get_game_platform_by_id(game_id, platform_id)

        if game_platform:
            return {'message': 'Game platform already exists!'}
        
        return self.game_platform_repository.create_game_platform(game_id, platform_id)

    def delete_game_platform(self, game_id, platform_id):
        return self.game_platform_repository.delete_game_platform(game_id, platform_id)

    def get_platform_by_game(self, game_id):
        return self.game_platform_repository.get_all_platforms(game_id)

    def get_game_by_platform(self, platform_id):
        return self.game_platform_repository.get_all_games(platform_id)