from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserSchema

def seed_users(user_repository: UserRepository= UserRepository()):
    user = {
        'email': 'felipe@email.com',
        'username': 'gaby',
        'password': '1234',
        'bio': 'I am a software engineer',
    }

    user = UserSchema().load(user)

    user_repository.create(user)
    print('Users seeded!')



