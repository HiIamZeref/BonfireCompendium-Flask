from app.repositories.developer_repository import DeveloperRepository
from app.schemas.developer_schema import DeveloperSchema

def seed_developers(developer_repository: DeveloperRepository= DeveloperRepository()):
    developers = [
        {
            'name': 'FromSoftware'
        },
        {
            'name': 'Naughty Dog'
        },
        {
            'name': 'Rockstar Games'
        },
        {
            'name': 'CD Projekt Red'
        },
        {
            'name': 'Nintendo'
        },
        {
            'name': 'Capcom'
        },
        {
            'name': 'Square Enix'
        },
        {
            'name': 'Konami'
        },
        {
            'name': 'Ubisoft'
        },
        {
            'name': 'Bethesda'
        }
    ]

    for developer in developers:
        developer = DeveloperSchema().load(developer)
        developer_repository.create(developer)

    print('Developers seeded!')