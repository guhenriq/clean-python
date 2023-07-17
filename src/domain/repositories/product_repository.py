from abc import ABC, abstractmethod
from src.domain.entities.product import Product


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def create_product(id: int, name: str, value: float) -> bool: pass

    @abstractmethod
    def find_product(id: int) -> Product: pass