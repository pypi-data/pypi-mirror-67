import pytest
from flaskr import db
from flaskr.model import User


testdata = [
    ('xyz@gmail.com', '123456'),
    ('blah@yahoo.com', '454545'),
    ('something@illinois.edu', 'whatever'),
    ('a2z@gmail.com', 'What%%123')
]

@pytest.mark.parametrize("email, password", testdata)
def test_register_no_error(client, email, password):
    res = client.post('/register', json={
        "email": email,
        "password": password
    })
    assert res.status_code == 200
    assert "errorMsg" not in res.json

@pytest.mark.parametrize("email, password", testdata)
def test_register_user_in_database(client, email, password):
    res = client.post('/register', json={
        "email": email,
        "password": password
    })
    assert res.status_code == 200
    assert "errorMsg" not in res.json

    user = db.session.query(User).filter_by(email=email).one()
    assert user.email == email


@pytest.mark.parametrize("email, password", testdata)
def test_register_duplicate(client, email, password):
    res = client.post('/register', json={
        "email": email,
        "password": password
    })
    assert res.status_code == 200
    assert "errorMsg" not in res.json
    res = client.post('/register', json={
        "email": email,
        "password": password
    })
    assert res.status_code == 200
    assert res.json['errorMsg'] == 'User already exists'


def test_register_invalid_email(client):
    res = client.post('/register', json={
        "email": 'blah@@',
        "password": 'password'
    })
    assert res.status_code == 200
    assert res.json['errorMsg'] == 'Invalid email'



def test_register_empty_password(client):
    res = client.post("/register", json={
        "email": 'xyz@gmail.com',
        "password": ''
    })
    assert res.status_code == 200
    assert "errorMsg" in res.json
    assert res.json['errorMsg'] == 'Password field is empty'

def test_register_empty_email(client):
    res = client.post("/register", json={
        "email": '',
        "password": 'password'
    })
    assert res.status_code == 200
    assert "errorMsg" in res.json
    assert res.json['errorMsg'] == 'Email field is empty'

def test_register_email_case_insensitive(client):
    res = client.post('/register', json={
        "email": 'abc@gmail.com',
        "password": 'password'
    })
    assert res.status_code == 200
    assert "errorMsg" not in res.json
    res = client.post('/register', json={
        "email": 'ABC@GMAIL.COM',
        "password": 'password'
    })
    assert res.status_code == 200
    assert res.json['errorMsg'] == 'User already exists'

