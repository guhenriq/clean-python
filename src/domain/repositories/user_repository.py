from abc import ABC, abstractmethod
from src.domain.entities.user import User


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create_user(id: int, name: str, email: str, password: str) -> bool: pass

    @abstractmethod
    def find_user(email: str) -> User: pass