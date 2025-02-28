from http import HTTPStatus

from fastapi.testclient import TestClient
from to_do_list.app import app
from datetime import datetime
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache import FastAPICache

def test_create_tarefa():
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

def test_leitura_tarefas_schema():
    # Cliente de teste
    client = TestClient(app)
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    response = client.get('/tarefa/')

    tarefas = response.json().get('tarefas', [])
    assert isinstance(tarefas, list), f"Esperado uma lista, mas recebeu {type(tarefas)}"

    for tarefa in tarefas:
        assert 'id' in tarefa, f"Tarefa {tarefa} não possui o campo 'id'"
        assert 'titulo' in tarefa, f"Tarefa {tarefa} não possui o campo 'titulo'"
        assert 'descricao' in tarefa, f"Tarefa {tarefa} não possui o campo 'descricao'"
        assert 'estado' in tarefa, f"Tarefa {tarefa} não possui o campo 'estado'"
        assert 'data_criacao' in tarefa, f"Tarefa {tarefa} não possui o campo 'data_criacao'"
        assert 'data_atualizacao' in tarefa, f"Tarefa {tarefa} não possui o campo 'data_atualizacao'"

    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"

def test_atualizacao_tarefa(token, usuario):
    client = TestClient(app)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.put('/tarefa/2',
                          json={
                            'id': 2,
                            'titulo': "Primeira Tarefa",
                            'descricao': "realizando a primeira tarefa",
                            'estado': 'pendente',
                            'data_criacao': datetime.now().isoformat(),
                            'data_atualizacao': datetime.now().isoformat()
                        },
                        headers=headers)
    assert response.status_code == HTTPStatus.OK
'''
def teste_deletar_tarefa():
    client = TestClient(app)
    response = client.delete("/tarefa/4")
    assert response.status_code == HTTPStatus.OK
'''