from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app import db, bcrypt
from app.models.user import User




class UserRepository:
    def __init__(
        self,
        db: SQLAlchemy = db,
        bcrypt: Bcrypt = bcrypt) -> None:

        self.db = db
        self.bcrypt = bcrypt


    def create(self, data):
        password = data.pop('password')
        hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')
        data['password'] = hashed_password

        user = User(**data)
        
        self.db.session.add(user)
        self.db.session.commit()
        return user
    
    def get(self, id):
        return User.query.get(id)
    
    def get_all(self):
        return User.query.all()
    
    def update(self, user, data):
        for key, value in data.items():
            setattr(user, key, value)
        
        self.db.session.commit()
        return user
    
    def delete(self, user):
        self.db.session.delete(user)
        self.db.session.commit()
        return user
    
    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()
    
    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()
    
    