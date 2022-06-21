import pytest
from app import create_app
from assertpy import assert_that

# Creating the fixtures for the test to be able to call the app routes
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

# Tests for each one of the views in the app   
def test_homepage_up(client):
    assert client.get('/').status_code == 200
def test_deportes(client):
    response = client.get('/deportes')
    assert b"Deportes" in response.data
def test_elpais(client):
    response = client.get('/elpais')
    assert_that(response.data).contains(b"El Pais")
def test_mundo(client):
    response = client.get('/mundo')
    assert_that(response.data).contains(b"Mundo")
def test_tecnologia(client):
    response = client.get('/tecnologia')
    assert_that(response.data).contains(b"Tecnologia")
def test_economia(client):
    response = client.get('/economia')
    assert_that(response.data).contains(b"Economia")

# Test for El Financiero views in the app
def test_economia_ef(client):
    response = client.get('/economia_ef')
    assert_that(response.data).contains(b"Economia")

def test_opinion_ef(client):
    response = client.get('/opinion_ef')
    assert_that(response.data).contains(b"Opinion")

def test_pymes_ef(client):
    response = client.get('/pymes_ef')
    assert_that(response.data).contains(b"Pymes")

def test_tecnologia_ef(client):
    response = client.get('/tecnologia_ef')
    assert_that(response.data).contains(b"Tecnologia")