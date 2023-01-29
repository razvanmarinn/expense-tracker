"""User DTO class"""
from src.models import User

class UserDTO:
    """User Data Transfer Object class"""
    def __init__(self, user: User):
        self.id = user.id
        self.username = user.username
