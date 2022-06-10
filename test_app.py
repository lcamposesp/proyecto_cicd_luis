import pytest
from app import create_app

@pytest.fixture
def app():
    app=create_app()
    yield app
@pytest.fixture
def client(app):
    return app.test_client()
@pytest.fixture
def runner(app):
    return app.test_cli_runner()
def test_homepage_up(client):
    assert client.get('/').status_code == 200
def test_deportes(client):
    response = client.get('/deportes')
    assert b"Deportes" in response.data
