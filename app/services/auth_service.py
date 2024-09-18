from app.repositories.user_repository import UserRepository
from flask_jwt_extended import create_access_token, create_refresh_token

class AuthService:
    """
    Service class for managing user authentication.

    This class provides methods to register, login, and logout users.
    It interacts with the UserRepository to perform database operations.

    Methods:
    --------
    __init__():
        Initializes the AuthService with a UserRepository instance.

    login(username: str, password: str) -> dict:
        Logs in a user.
        - Parameters:
            - username (str): The username of the user.
            - password (str): The password of the user.
        - Returns:
            - dict: A message indicating whether the login was successful.

    refresh(current_user_id: int) -> dict:
        Refreshes the access token for the current user.
        - Parameters:
            - current_user_id (int): The ID of the current user.
        - Returns:
            - dict: A new access token.

    logout() -> dict:
        Logs out the current user.
        - Returns:
            - dict: A message indicating whether the logout was successful.
    """
    
    def __init__(self):
        self.user_repository = UserRepository()


    def login(self, username, password):
        # Check if user exists
        user = self.user_repository.get_by_username(username)

        # Check password
        if user and self.user_repository.check_password(user.password, password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        
        return {'message': 'Invalid credentials'}
    
    def refresh(self, current_user_id):
        new_access_token = create_access_token(identity=current_user_id, fresh=False)
        return {'access_token': new_access_token}

    def logout(self):
        # Placeholder for logout functionality
        return {'message': 'Logout successful!'}