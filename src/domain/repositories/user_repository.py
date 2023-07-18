from abc import ABC, abstractmethod
from src.domain.entities.user import User


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create_user(user: User) -> any: pass

    @abstractmethod
    def find_user_by_email(email: str) -> User: pass