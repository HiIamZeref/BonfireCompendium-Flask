from app.repositories.genre_repository import GenreRepository
from app.schemas.genre_schema import GenreSchema

def seed_genres(genre_repository: GenreRepository= GenreRepository()):
    genres = [
        {
            'name': 'Indie',
        },
        {
            'name': 'Soulslike',
        },
        {
            'name': 'Action',
        },
        {
            'name': 'Adventure',
        },
        {
            'name': 'RPG',
        },
        {
            'name': 'Simulation',
        },
        {
            'name': 'Strategy',
        },
        {
            'name': 'Sports',
        },
        {
            'name': 'Puzzle',
        },
        {
            'name': 'Idle',
        },
        {
            'name': 'Casual',
        },
        {
            'name': 'Arcade',
        },
        {
            'name': 'Racing',
        },
        {
            'name': 'Horror',
        },
        {
            'name': 'Survival',
        },
        {
            'name': 'Shooter',
        },
        {
            'name': 'Fighting',
        },
        {
            'name': 'MMO',
        },
        {
            'name': 'MOBA',
        },
        {
            'name': 'Battle Royale',
        },
        {
            'name': 'Sandbox',
        },
        {
            'name': 'Open World',
        },
        {
            'name': 'MMORPG',
        },
        {
            'name': 'Metroidvania',
        },
        {
            'name': 'Stealth',
        },
        {
            'name': 'Platformer',
        },
        {
            'name': 'Roguelike',
        },
        {
            'name': 'Rhythm',
        },
        {
            'name': 'Educational',
        },
        {
            'name': 'Music',
        },
        {
            'name': 'Party',
        },
        {
            'name': 'Trivia',
        },
        {
            'name': 'Board',
        },
        {
            'name': 'Cards',
        },
        {
            'name': 'Puzzle Adventure',
        },
        
    ]

    for genre in genres:
        genre = GenreSchema().load(genre)
        genre_repository.create(genre)

    print('Genres seeded!')