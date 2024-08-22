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
    
    def get(self, id):
        return User.query.get(id)
    
    def get_all(self):
        return User.query.all()
    
    def update(self, user, data):
        for key, value in data.items():
            setattr(user, key, value)
        
        db.session.commit()
        return user
    
    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
        return user
    
    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()
    
    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()
    
    