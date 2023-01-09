import pytest
from website.models import UserModel
@pytest.mark.usefixtures('client')
def test_login_invalid_client(client):

    response = client.post('/auth/login', data={'username': 'asd', 'password': 'test'}, follow_redirects=True)
    assert b'Invalid username or password' in response.data


@pytest.mark.usefixtures('client')
def test_login_valid_username(client):
    response = client.post('/auth/login', data={'username': 'asd', 'password': 'asd'} )
    assert response.status_code == 302
    response = client.get('/')
    assert b'<h1> Home</h1>\n' in response.data


@pytest.mark.usefixtures('client')
def test_create_user(client):
    user_model = UserModel()
    response = client.post('/auth/sign-up', data={'username': 'test999', 'password': 'test', 'email': 'asd@asd.ro'} )
    assert response.status_code == 302
    response = client.get('/')
    user = user_model.get_user_by_username('test999')
    assert user is not None
    user_model.delete_user_by_username('test999')
    assert b'<h1> Home</h1>\n' in response.data


@pytest.mark.usefixtures('client')
def test_create_user_username_already_used(client):
    user_model = UserModel()
    response = client.post('/auth/sign-up', data={'username': 'asd', 'password': 'asd', 'email': 'asd@asd.ro'} )
    assert response.status_code == 200
    user = user_model.get_user_by_username('asd')
    assert user is not None
    assert b'Username already used' in response.data