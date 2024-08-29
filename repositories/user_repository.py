from entities.user import User

class UserRepository:
    def __init__(self):
        self.users = []

    def save(self, user: User):
        self.users.append(user)

    def find_by_id(self, identification):
        for user in self.users:
            if user._identification == identification:
                return user
        return None