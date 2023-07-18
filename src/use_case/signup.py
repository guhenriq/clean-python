from src.domain.entities import User
from src.domain.repositories import UserRepositoryInterface


class SignUp:

    def __init__(self, user_repo: UserRepositoryInterface) -> None:
        self.user_repo = user_repo

    def execute(self, user_name: str, user_email: str, user_password: str) -> None:
        user_exists = self.user_repo.find_user_by_email(user_email)

        if user_exists:
            raise Exception("User already exists")

        new_user = User(user_name, user_email, user_password)

        self.user_repo.create_user(new_user)