from .user import User
from .product import Product

class Order:

    def __init__(self, order_number: int, user: User, product: Product) -> None:
        self.order_number = order_number
        self.user = user
        self.product = product