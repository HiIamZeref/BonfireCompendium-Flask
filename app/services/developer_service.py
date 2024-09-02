from app.repositories.developer_repository import DeveloperRepository

class DeveloperService:
    def __init__(self,
                 developer_repository: DeveloperRepository = DeveloperRepository()) -> None:
        self.developer_repository = developer_repository

    def get(self, id):
        '''
        Get a developer by ID
        '''
        return self.developer_repository.get(id)
    
    def get_all(self):
        '''
        List all developers
        '''
        return self.developer_repository.get_all()
        