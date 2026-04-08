import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_get_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_post_vazio(client):
    response = client.post('/', data={'mensagem': ''})
    assert b"Por favor, digite uma pergunta." in response.data

def test_post_valido(client):
    response = client.post('/', data={'mensagem': 'oi'})
    assert b"Bem-vindo" in response.data