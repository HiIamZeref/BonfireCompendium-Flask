from app.repositories.publisher_repository import PublisherRepository

class PublisherService:
    """
    Service layer for Publisher operations.

    This class provides methods to interact with the PublisherRepository.
    It includes methods to retrieve a single publisher by ID and to retrieve all publishers.

    Attributes:
    ----------
    publisher_repository : PublisherRepository
        The repository instance used to interact with the publisher data.

    Methods:
    -------
    get(id: int) -> Publisher:
        Retrieves a publisher by its ID.
    get_all() -> list[Publisher]:
        Retrieves all publishers.
    """

    def __init__(self, publisher_repository: PublisherRepository = PublisherRepository()) -> None:
        """
        Initializes the PublisherService with the given PublisherRepository instance.

        Parameters:
        ----------
        publisher_repository : PublisherRepository, optional
            The repository instance used to interact with the publisher data (default is a new PublisherRepository instance).
        """
        self.publisher_repository = publisher_repository

    def get(self, id):
        """
        Get a publisher by ID.

        Parameters:
        ----------
        id : int
            The ID of the publisher to retrieve.

        Returns:
        -------
        Publisher
            The Publisher object with the specified ID, or None if not found.
        """
        return self.publisher_repository.get(id)
    
    def get_all(self):
        """
        Get all publishers.

        Returns:
        -------
        list[Publisher]
            A list of all Publisher objects.
        """
        return self.publisher_repository.get_all()