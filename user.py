# user.py
from models import User
import storage

class UserManager:
    def __init__(self):
        self.users = storage.load_users()

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        storage.save_users(self.users)

    def list_users(self):
        for user in self.users:
            print(user)

    def find_user(self, **kwargs):
        for user in self.users:
            if all(getattr(user, k) == v for k, v in kwargs.items()):
                return user
        return None
