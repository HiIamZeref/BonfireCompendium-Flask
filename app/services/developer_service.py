from app.repositories.developer_repository import DeveloperRepository

class DeveloperService:
    def __init__(self,
                 developer_repository: DeveloperRepository = DeveloperRepository()) -> None:
        self.developer_repository = developer_repository

    def get(self, id):
        return self.developer_repository.get(id)
    
    def get_all(self):
        return self.developer_repository.get_all()
        