from app.repositories.platform_repository import PlatformRepository
from app.schemas.platform_schema    import PlatformSchema

def seed_platforms(platform_repository: PlatformRepository = PlatformRepository()):
    platforms = [
        {
            'name': 'PC'
        },
        {
            'name': 'PlayStation 4'
        },
        {
            'name': 'Xbox One'
        },
        {
            'name': 'Nintendo Switch'
        },
        {
            'name': 'PlayStation 5'
        },
        {
            'name': 'Xbox Series X'
        },
        {
            'name': 'iOS'
        },
        {
            'name': 'Android'
        }
    ]

    for platform in platforms:
        platform = PlatformSchema().load(platform)
        platform_repository.create(platform)

    print('Platforms seeded!')