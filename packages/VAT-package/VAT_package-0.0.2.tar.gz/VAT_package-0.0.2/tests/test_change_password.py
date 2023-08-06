import pytest
from .test_login import register_random_user
from .conftest import create_auth_header

def test_success(client):

    email = 'test@illinois.edu'
    password = '123456'
    auth_headers = create_auth_header(client, email=email, password=password)

    body = {}
    body['oldPass'] = password
    body['newPass'] = "test"
    res = client.post("/changePass", json=body, headers=auth_headers)
    assert res.status_code == 200
    user = {
        'email': email,
        'password': body['newPass']
    }
    res = client.post("/login", json=user)
    assert res.status_code == 200

def test_authorization(client):
    body = {
        'oldPass': '123456',
        'newPass': 'test'
    }
    res = client.post("/changePass", json=body)
    assert res.status_code == 401

def test_wrong_password(client):

    email = 'test@illinois.edu'
    password = '123456'
    auth_headers = create_auth_header(client, email=email, password=password)

    body = {}
    body['oldPass'] = 'wrong password'
    body['newPass'] = "test"
    res = client.post("/changePass", json=body, headers=auth_headers)
    assert res.status_code == 200
    assert res.json['errorMsg'] == 'Wrong password'

@pytest.mark.parametrize("passwrd_num", [1, 2, 3, 4, 5])
def test_multiple_change_password(client, passwrd_num):

    email = 'test@illinois.edu'
    password = f'123456'
    auth_headers = create_auth_header(client, email=email, password=password)

    body = {
        'oldPass': password,
        'newPass': f'<test{passwrd_num}>'
    }

    res = client.post("/changePass", json=body, headers=auth_headers)
    assert res.status_code == 200
    user = {
        'email': email,
        'password': body['newPass']
    }
    res = client.post("/login", json=user)
    assert res.status_code == 200

