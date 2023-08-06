import pytest

testdata = [
    ('xyz@gmail.com', '123456'),
    ('blah@yahoo.com', '454545'),
    ('something@illinois.edu', 'whatever'),
    ('a2z@gmail.com', 'What%%123')
]

@pytest.mark.parametrize("email, password", testdata)
def test_login_success(client, email, password):
    user = register_random_user(client, email, password)
    res = client.post("/login", json=user)
    assert res.status_code == 200
    assert "access_token" in res.json

@pytest.mark.parametrize("email, password", testdata)
def test_login_incorrect_password(client, email, password):
    register_random_user(client, email, password)
    res = client.post("/login", json={
        "email": email,
        "password": "incorrectpassword"
    })
    assert res.status_code == 200
    assert "errorMsg" in res.json
    assert res.json['errorMsg'] == 'Wrong password'

@pytest.mark.parametrize("email, password", testdata)
def test_login_empty_email(client, email, password):
    register_random_user(client, email, password)
    res = client.post("/login", json={
        "email": '',
        "password": password
    })
    assert res.status_code == 200
    assert "errorMsg" in res.json
    assert res.json['errorMsg'] == 'Email field is empty'

@pytest.mark.parametrize("email, password", testdata)
def test_login_empty_password(client, email, password):
    register_random_user(client, email, password)
    res = client.post("/login", json={
        "email": email,
        "password": ''
    })
    assert res.status_code == 200
    assert "errorMsg" in res.json
    assert res.json['errorMsg'] == 'Password field is empty'

def test_login_unregistered_user(client):
    res = client.post("/login", json={
        "email": "random@illinois.edu",
        "password": "123456"
    })
    assert res.status_code == 200
    assert "errorMsg" in res.json
    assert res.json['errorMsg'] == 'User not registered'



def register_random_user(client, email, password):
    user = {
        "email": email,
        "password": password
    }
    #register user
    res = client.post("/register", json=user)
    assert res.status_code == 200
    return user
