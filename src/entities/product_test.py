from .product import Product

def test_instance_new_product():
    mocked_product_id = 1
    mocked_product_name = "Apple Watch"
    mocked_product_value = 1999.90

    new_product = Product(mocked_product_id, mocked_product_name, mocked_product_value)
    
    assert new_product.id == mocked_product_id
    assert mocked_product_name == mocked_product_name
    assert mocked_product_value == mocked_product_value
