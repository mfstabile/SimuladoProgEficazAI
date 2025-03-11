import pytest
from unittest.mock import patch, MagicMock
from app import app, conectar_bd  # Importamos a aplicação Flask e a função de conexão

@pytest.fixture
def client():
    """Cria um cliente de teste para a API."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("app.conectar_bd")
def test_get_usuarios(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        (1, "Alice", "alice@email.com", 30),
        (2, "Bob", "bob@email.com", 25)
    ]
    mock_conectar_bd.return_value = mock_conn

    response = client.get("/usuarios")
    assert response.status_code == 200
    assert response.get_json() == [
        {"id": 1, "nome": "Alice", "email": "alice@email.com", "idade": 30},
        {"id": 2, "nome": "Bob", "email": "bob@email.com", "idade": 25}
    ]

@patch("app.conectar_bd")
def test_get_usuario(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = (1, "Alice", "alice@email.com", 30)
    mock_conectar_bd.return_value = mock_conn

    response = client.get("/usuarios/1")
    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "nome": "Alice", "email": "alice@email.com", "idade": 30}

@patch("app.conectar_bd")
def test_get_usuario_404(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None
    mock_conectar_bd.return_value = mock_conn

    response = client.get("/usuarios/999")
    assert response.status_code == 404
    assert response.get_json() == {"erro": "Usuário não encontrado"}

@patch("app.conectar_bd")
def test_post_usuario(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conectar_bd.return_value = mock_conn

    response = client.post("/usuarios", json={"nome": "Carlos", "email": "carlos@email.com", "idade": 28})
    assert response.status_code == 201
    assert response.get_json() == {"mensagem": "Usuário criado com sucesso"}

@patch("app.conectar_bd")
def test_post_postagem(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conectar_bd.return_value = mock_conn

    response = client.post("/postagens", json={"conteudo": "Minha primeira postagem", "id_usuario": 1})
    assert response.status_code == 201
    assert response.get_json() == {"mensagem": "Postagem criada com sucesso"}

@patch("app.conectar_bd")
def test_get_postagem(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = (1, "Minha primeira postagem", 1)
    mock_conectar_bd.return_value = mock_conn

    response = client.get("/postagens/1")
    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "conteudo": "Minha primeira postagem", "id_usuario": 1}

@patch("app.conectar_bd")
def test_get_postagem_404(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None
    mock_conectar_bd.return_value = mock_conn

    response = client.get("/postagens/999")
    assert response.status_code == 404
    assert response.get_json() == {"erro": "Postagem não encontrada"}

@patch("app.conectar_bd")
def test_get_postagens(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        (1, "Minha primeira postagem", 1),
        (2, "Outra postagem", 2)
    ]
    mock_conectar_bd.return_value = mock_conn

    response = client.get("/postagens")
    assert response.status_code == 200
    assert response.get_json() == [
        {"id": 1, "conteudo": "Minha primeira postagem", "id_usuario": 1},
        {"id": 2, "conteudo": "Outra postagem", "id_usuario": 2}
    ]

@patch("app.conectar_bd")
def test_get_postagens_usuario(mock_conectar_bd, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        (1, "Minha primeira postagem", 1)
    ]
    mock_conectar_bd.return_value = mock_conn

    response = client.get("/usuarios/1/postagens")
    assert response.status_code == 200
    assert response.get_json() == [
        {"id": 1, "conteudo": "Minha primeira postagem", "id_usuario": 1}
    ]
