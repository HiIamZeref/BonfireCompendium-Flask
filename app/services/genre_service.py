from app.repositories.genre_repository import GenreRepository

class GenreService:
    """
    Service layer for Genre operations.

    This class provides methods to interact with the GenreRepository.
    It includes methods to retrieve a single genre by ID and to retrieve all genres.

    Attributes:
    ----------
    genre_repository : GenreRepository
        The repository instance used to interact with the genre data.

    Methods:
    -------
    get(id: int) -> Genre:
        Retrieves a genre by its ID.
    get_all() -> list[Genre]:
        Retrieves all genres.
    """

    def __init__(self, genre_repository: GenreRepository = GenreRepository()) -> None:
        """
        Initializes the GenreService with the given GenreRepository instance.

        Parameters:
        ----------
        genre_repository : GenreRepository, optional
            The repository instance used to interact with the genre data (default is a new GenreRepository instance).
        """
        self.genre_repository = genre_repository

    def get(self, id):
        """
        Get a genre by ID.

        Parameters:
        ----------
        id : int
            The ID of the genre to retrieve.

        Returns:
        -------
        Genre
            The Genre object with the specified ID, or None if not found.
        """
        return self.genre_repository.get(id)
    
    def get_all(self):
        """
        Get all genres.

        Returns:
        -------
        list[Genre]
            A list of all Genre objects.
        """
        return self.genre_repository.get_all()