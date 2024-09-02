from app.repositories.game_status_repository import GameStatusRepository
from app.schemas.game_status_schema import GameStatusSchema

def seed_game_statuses(game_status_repository: GameStatusRepository= GameStatusRepository()):
    game_statuses = [
        {
            'name': 'Played',
        },
        {
            'name': 'Playing',
        },
        {
            'name': 'Completed'
        },
        {
            'name': 'Retired'
        },
        {
            'name': 'Shelved'
        },
        {
            'name': 'Abandoned'
        }
        
    ]

    for game_status in game_statuses:
        game_status = GameStatusSchema().load(game_status)
        game_status_repository.create(game_status)

    print('Game statuses seeded!')