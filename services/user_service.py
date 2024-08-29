from repositories.user_repository import UserRepository
from entities.user import User

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register_user(self, identification, names, age):
        user = User(identification, names, age)
        self.repository.save(user)
        return user