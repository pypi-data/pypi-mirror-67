import pytest
from flaskr import create_app, db
import sqlite3

@pytest.fixture
def app():
    app = create_app()
    clear_database()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers(client):
    return create_auth_header(client)

# same as auth headers but for another user
@pytest.fixture
def auth_headers2(client):
    return create_auth_header(client, email='testuser2@illinois.edu')

def clear_database():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()

def create_auth_header(client, email="testuser@illinois.edu", password="123456"):
    user = {
        "email": email,
        "password": password
    }
    client.post("/register", json=user)
    res = client.post("/login", json=user)
    assert res.status_code == 200
    assert "access_token" in res.json
    return {'Authorization': 'Bearer ' + res.json['access_token']}
