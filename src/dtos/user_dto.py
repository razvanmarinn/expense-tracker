"""User DTO class"""


class UserDTO:
    """User Data Transfer Object class"""
    def __init__(self, username: str, user_id: int):
        self.id = user_id
        self.username = username
