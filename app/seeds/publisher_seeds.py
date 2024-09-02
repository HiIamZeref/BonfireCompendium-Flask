from app.repositories.publisher_repository import PublisherRepository
from app.schemas.publisher_schema import PublisherSchema

def seed_publishers(publisher_repository: PublisherRepository= PublisherRepository()):
    publishers = [
        {
            'name': 'Banda Namco'
        },
        {
            'name': 'Sony Interactive Entertainment'
        },
        {
            'name': 'Rockstar Games'
        },
        {
            'name': 'CAPCOM'
        },
        {
            'name': 'Nintendo'
        },
        {
            'name': 'Square Enix'
        },
        {
            'name': 'Ubisoft'
        },
        {
            'name': 'Bethesda Softworks'
        },
        {
            'name': 'Activision'
        },
        {
            'name': 'Electronic Arts'
        }
    ]

    for publisher in publishers:
        publisher = PublisherSchema().load(publisher)
        publisher_repository.create(publisher)

    print('Publishers seeded!')