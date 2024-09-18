from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository = UserRepository()) -> None:
        self.user_repository = user_repository

    
    def create(self, validated_data):
        # Check if email already exists
        user = self.user_repository.get_by_email(validated_data['email'])
        if user:
            return {'message': 'Email already exists!'}
        
        # Check if username already exists
        user = self.user_repository.get_by_username(validated_data['username'])
        if user:
            return {'message': 'Username already exists!'}
        
        return self.user_repository.create(validated_data)
    
    def get(self, id):
        return self.user_repository.get(id)
    
    def get_all(self):
        return self.user_repository.get_all()
    
    def update(self, user, validated_data):
        return self.user_repository.update(user, validated_data)
    
    def delete(self, user):
        return self.user_repository.delete(user)
    
    def change_password(self, user, validated_data):
        # Check if old password is correct
        if not self.user_repository.check_password(user.password, validated_data['old_password']):
            return {'message': 'Invalid credentials!'}
        
        # Check if new password is the same as old password
        if validated_data['old_password'] == validated_data['new_password']:
            return {'message': 'New password cannot be the same as old password!'}
        
        
        return self.user_repository.change_password(user, validated_data)
    

        