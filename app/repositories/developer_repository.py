from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.developer import Developer

class DeveloperRepository:
    def __init__(self,
                 db: SQLAlchemy = db) -> None:
        self.db = db
    
    def get(self, id):
        '''
        Get a developer by ID
        '''
        return Developer.query.get(id)
    
    def get_all(self):
        '''
        List all developers
        '''
        return Developer.query.all()
    
    def create(self, developer):
        '''
        Create a new developer
        '''
        developer = Developer(**developer)

        self.db.session.add(developer)
        self.db.session.commit()
        return developer
    
    def update(self, developer, data):
        '''
        Update a developer
        '''

        for key, value in data.items():
            setattr(developer, key, value)

        self.db.session.commit()

    def delete(self, developer):
        '''
        Delete a developer
        '''
        self.db.session.delete(developer)
        self.db.session.commit()

        