from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models.developer import Developer

class DeveloperRepository:
    def __init__(self,
                 db: SQLAlchemy = db) -> None:
        self.db = db
    
    def get(self, id):
        return Developer.query.get(id)
    
    def get_all(self):
        return Developer.query.all()
        