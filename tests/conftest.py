import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from to_do_list.app import app
from to_do_list.models import table_registry, TarefaDB
from to_do_list.database import get_session

@pytest.fixture
def client():
    def get_session_override():
        return session
    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client
    app.dependency_overrides.clear()

@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool)
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
    
    table_registry.metadata.drop_all(engine)

@pytest.fixture
def tarefa(session):
    tarefa = TarefaDB(
        titulo="Titulo",
        descricao="Descricao",
        estado="em andamento"
        )
    return tarefa
