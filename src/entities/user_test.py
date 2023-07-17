from .user import User

def test_instance_new_user():
    mocked_user_id = 1,
    mocked_user_name = "Teste"
    mocked_user_email = "teste@gmail.com"
    mocked_user_password = "teste123"

    new_user = User(mocked_user_id, mocked_user_name, mocked_user_email, mocked_user_password)

    assert new_user.id == mocked_user_id
    assert new_user.name == mocked_user_name
    assert new_user.email == mocked_user_email
    assert new_user.password == mocked_user_password
