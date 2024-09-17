from app.repositories.game_repository import GameRepository
from app.schemas.game_schema import CreateOrDeleteGameSchema

def seed_games(game_repository: GameRepository = GameRepository()):
    games = [
        {
            'title': 'The Legend of Zelda: Breath of the Wild',
            'description': 'The Legend of Zelda: Breath of the Wild is an action-adventure game developed and published by Nintendo. An entry in the longrunning The Legend of Zelda series, it was released for the Nintendo Switch and Wii U consoles on March 3, 2017.',
            'release_date': '2017-03-03',
            'genre_id': 4,
            'developer_id': 5,
            'publisher_id': 5,
        },
        {
            'title': 'Dark Souls III',
            'description': 'Dark Souls III is an action role-playing game developed by FromSoftware and published by Bandai Namco Entertainment. It was released for PlayStation 4, Xbox One, and Microsoft Windows in Japan in March 2016 and worldwide in April 2016.',
            'release_date': '2016-03-24',
            'genre_id': 2,
            'developer_id': 1,
            'publisher_id': 1,
        },
        {
            'title': 'Bloodborne',
            'description': 'Bloodborne is an action role-playing game developed by FromSoftware and published by Sony Computer Entertainment, which released for the PlayStation 4 in March 2015.',
            'release_date': '2015-03-24',
            'genre_id': 2,
            'developer_id': 1,
            'publisher_id': 2,
        },
        {
            'title': 'The Witcher 3: Wild Hunt',
            'description': 'The Witcher 3: Wild Hunt is an action role-playing game developed and published by CD Projekt. Based on The Witcher series of fantasy novels by Polish author Andrzej Sapkowski, it is the sequel to the 2011 game The Witcher 2: Assassins of Kings.',
            'release_date': '2015-05-19',
            'genre_id': 5,
            'developer_id': 4,
            'publisher_id': 4,
        },
        {
            'title': 'Red Dead Redemption 2',
            'description': 'Red Dead Redemption 2 is a 2018 action-adventure game developed and published by Rockstar Games. The game is the third entry in the Red Dead series and is a prequel to the 2010 game Red Dead Redemption.',
            'release_date': '2018-10-26',
            'genre_id': 4,
            'developer_id': 3,
            'publisher_id': 3,
        },
        {
            'title': 'Grand Theft Auto V',
            'description': 'Grand Theft Auto V is a 2013 action-adventure game developed by Rockstar North and published by Rockstar Games. It is the first main entry in the Grand Theft Auto series since 2008\'s Grand Theft Auto IV.',
            'release_date': '2013-09-17',
            'genre_id': 4,
            'developer_id': 3,
            'publisher_id': 3,
        },
        {
            'title': 'Persona 5 Royal',
            'description': 'Persona 5 Royal is a role-playing video game developed by Atlus. It is a re-release of Persona 5, which was released for the PlayStation 3 and PlayStation 4 in 2016.',
            'release_date': '2020-03-31',
            'genre_id': 5,
            'developer_id': 6,
            'publisher_id': 6,
        },
        {
            'title': 'Elden Ring',
            'description': 'Elden Ring is an upcoming action role-playing game developed by FromSoftware and published by Bandai Namco Entertainment. It is set to be released for Microsoft Windows, PlayStation 4, and Xbox One.',
            'release_date': '2022-02-25',
            'genre_id': 2,
            'developer_id': 1,
            'publisher_id': 1,
        }
    ]

    for game in games:
        game = CreateOrDeleteGameSchema().load(game)
        game_repository.create(game)

    print('Games seeded!')