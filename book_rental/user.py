# User Management: Classes and Instances
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserManager:
    def __init__(self): # Initialization Method
        self.users = {} # Dictionary

    def add_user(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = User(username, password)

    def authenticate(self, username, password):
        user = self.users.get(username)
        if not user or user.password != password:
            return False
        return True
