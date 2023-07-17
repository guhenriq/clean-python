from abc import ABC, abstractmethod
from src.domain.entities.user import User
from src.domain.entities.product import Product	
from src.domain.entities.order import Order


class OrderRepositoryInterface(ABC):

    @abstractmethod
    def create_order(order_number: int, user: User, product: Product) -> bool: pass

    @abstractmethod
    def find_order(order_number: int) -> Order: pass