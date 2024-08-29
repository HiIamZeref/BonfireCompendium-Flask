from app.repositories import UserRepository
from app.schemas import UserSchema

def seed_users(user_repository: UserRepository= UserRepository()):
    user = {
        'email': 'felipe@email',
        'username': 'gaby',
        'password': '1234',
        'bio': 'I am a software engineer',
    }

    user = UserSchema().load(user)

    user_repository.create(user)
    print('Users seeded!')



