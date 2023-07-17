from .user import User
from .product import Product
from .order import Order

def test_intance_new_order():
    mocked_user_id = 1,
    mocked_user_name = "Teste"
    mocked_user_email = "teste@gmail.com"
    mocked_user_password = "teste123"

    new_user = User(mocked_user_id, mocked_user_name, mocked_user_email, mocked_user_password)

    mocked_product_id = 1
    mocked_product_name = "Apple Watch"
    mocked_product_value = 1999.90

    new_product = Product(mocked_product_id, mocked_product_name, mocked_product_value)

    mocked_order_number = 50
    mocked_order_user = new_user
    mocked_order_product = new_product

    new_order = Order(mocked_order_number, mocked_order_user, mocked_order_product)

    assert new_order.order_number == mocked_order_number
    assert new_order.user.id == mocked_user_id
    assert new_order.user.name == mocked_user_name
    assert new_order.user.email == mocked_user_email
    assert new_order.user.password == mocked_user_password
    assert new_order.product.id == mocked_product_id
    assert new_order.product.name == mocked_product_name
    assert new_order.product.value == mocked_product_value
