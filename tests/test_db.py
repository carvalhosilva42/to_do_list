from sqlalchemy import select

from to_do_list.models import TarefaDB

def test_create_tarefa(session):
    nova_tarefa = TarefaDB(titulo="Minha Tarefa", estado="pendente")
    session.add(nova_tarefa)
    session.commit()

    tarefa = session.scalar(select(TarefaDB).where(TarefaDB.titulo == 'Minha Tarefa'))

    assert tarefa.titulo == 'Minha Tarefa'