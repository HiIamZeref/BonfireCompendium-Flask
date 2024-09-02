from app.repositories.platform_repository import PlatformRepository

class PlatformService:
    """
    Service layer for Platform operations.

    This class provides methods to interact with the PlatformRepository.
    It includes methods to retrieve a single platform by ID and to retrieve all platforms.

    Attributes:
    ----------
    platform_repository : PlatformRepository
        The repository instance used to interact with the platform data.

    Methods:
    -------
    get(id: int) -> Platform:
        Retrieves a platform by its ID.
    get_all() -> list[Platform]:
        Retrieves all platforms.
    """

    def __init__(self, platform_repository: PlatformRepository = PlatformRepository()) -> None:
        """
        Initializes the PlatformService with the given PlatformRepository instance.

        Parameters:
        ----------
        platform_repository : PlatformRepository, optional
            The repository instance used to interact with the platform data (default is a new PlatformRepository instance).
        """
        self.platform_repository = platform_repository

    def get(self, id):
        """
        Get a platform by ID.

        Parameters:
        ----------
        id : int
            The ID of the platform to retrieve.

        Returns:
        -------
        Platform
            The Platform object with the specified ID, or None if not found.
        """
        return self.platform_repository.get(id)
    
    def get_all(self):
        """
        Get all platforms.

        Returns:
        -------
        list[Platform]
            A list of all Platform objects.
        """
        return self.platform_repository.get_all()