from models import User
from app import db, bcrypt

class UserRepository:
    def create(self, data):
        password = data.pop('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        data['password'] = hashed_password

        user = User(**data)
        
        db.session.add(user)
        db.session.commit()
        return user