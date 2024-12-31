from sqlalchemy import select

from to_do_list.models import Tarefa

def test_create_tarefa(session):
    nova_tarefa = Tarefa(titulo="Minha Tarefa", estado="pendente")
    session.add(nova_tarefa)
    session.commit()

    tarefa = session.scalar(select(Tarefa).where(Tarefa.titulo == 'Minha Tarefa'))

    assert tarefa.titulo == 'Minha Tarefa'