"""User DTO class"""
class UserDTO:
    """User Data Transfer Object class"""
    def __init__(self, username: str, user_id: int):
        self.id = user_id
        self.username = username

class UserDetailsDTO:
    """Details Data Transfer Object class"""
    def __init__(self, user_id: int, name: str, email: str, phone: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.phone = phone
