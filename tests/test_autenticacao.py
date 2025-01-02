from http import HTTPStatus

from fastapi.testclient import TestClient
from to_do_list.app import app
from datetime import datetime

def test_create_usuario():
    client = TestClient(app)
    response = client.post(
        '/usuario/',
        json={
            'id': 1,
            'email': "bruno@gmail.com",
            'senha': "teste",
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'email': "bruno@gmail.com"
    }

def test_leitura_usuarios_schema():
    # Cliente de teste
    client = TestClient(app)

    response = client.get('/tarefa/')

    usuarios = response.json().get('usuarios', [])
    assert isinstance(usuarios, list), f"Esperado uma lista, mas recebeu {type(usuarios)}"

    for tarefa in usuarios:
        assert 'id' in tarefa, f"Tarefa {tarefa} não possui o campo 'id'"
        assert 'email' in tarefa, f"Tarefa {tarefa} não possui o campo 'email'"
        assert 'senha' in tarefa, f"Tarefa {tarefa} não possui o campo 'senha'"

    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"

def test_atualizacao_usuario(usuario, token):
    client = TestClient(app)
    response = client.put(f'/usuario/{usuario.id}',
                          json={
                            'id': usuario.id,
                            'email': "bruno@gmail.com",
                            'senha': "teste"
                        },
                        headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == HTTPStatus.OK
'''
def teste_deletar_usuario():
    client = TestClient(app)
    response = client.delete("/usuario/2")
    assert response.status_code == HTTPStatus.OK
'''
def test_obter_token(usuario):
    client = TestClient(app)
    response = client.post(
        '/usuario/token/',
        data = {'username':usuario.email,'password':usuario.senha_limpa}
    )
    token = response.json()
    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token

