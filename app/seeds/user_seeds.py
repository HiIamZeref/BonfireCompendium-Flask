from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserSchema

def seed_users(user_repository: UserRepository= UserRepository()):
    user = {
        'email': 'felipe@email.com',
        'username': 'gaby',
        'password': '1234',
        'bio': 'I am a software engineer',
    }

    users = [
        {
        'email': 'felipe@email.com',
        'username': 'gaby',
        'password': '1234',
        'bio': 'I am a software engineer',
        },
        {
        'email': 'bibia@email.com',
        'username': 'bibiagaby',
        'password': '4321',
        'bio': 'I am a financial analyst',
        },
        {
        'email': 'haru@email.com',
        'username': 'kingharu',
        'password': '5678',
        'bio': 'I am the king of all that is golden!',
        }
    ]
    for user in users:
        user = UserSchema().load(user)
        user_repository.create(user)

    print('Users seeded!')



