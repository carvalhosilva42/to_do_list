from http import HTTPStatus

from fastapi.testclient import TestClient
from to_do_list.app import app
from datetime import datetime

def test_create_user():
    client = TestClient(app)
    response = client.post(
        '/tarefa/',
        json={
            'id': 1,
            'titulo': "Primeira Tarefa",
            'descricao': "realizando a primeira tarefa",
            'estado': 'pendente',
            'data_criacao': datetime.now().isoformat(),
            'data_atualizacao': datetime.now().isoformat()
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'titulo': "Primeira Tarefa",
        'descricao': "realizando a primeira tarefa",
    }