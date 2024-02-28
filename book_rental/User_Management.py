# User Management: oop concepts (Encapsulation and Data Abstraction)
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # In a real application, passwords should be hashed!

class UserManager:
    def __init__(self):
        self.users = {} # dictionary
# methods:
    def add_user(self, username, password):
        # Conditional Statements
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = User(username, password)

    def authenticate(self, username, password):
        user = self.users.get(username)
        if not user or user.password != password:
            return False
        return True
