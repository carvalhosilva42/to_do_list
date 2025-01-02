from fastapi import APIRouter
from http import HTTPStatus
import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from to_do_list.database import get_session
from to_do_list.models import TarefaDB, UsuarioDB
from to_do_list.schemas import TarefaList, Tarefa, TarefaPublic
from to_do_list.security import (
    obter_usuario_atual,
    obter_senha_hash,
)
router = APIRouter(prefix='/tarefa', tags=['tarefas'])

@router.post('/', status_code = HTTPStatus.CREATED, response_model=TarefaPublic)
def adiciona_tarefa(tarefa: Tarefa, session: Session = Depends(get_session)):
    db_tarefa = TarefaDB(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        estado=tarefa.estado
        )
    db_tarefa.data_criacao = datetime.datetime.now()
    db_tarefa.atualizacao = datetime.datetime.now()
    session.add(db_tarefa)
    session.commit()
    session.refresh(db_tarefa)
    return db_tarefa

@router.get('/', response_model=TarefaList)
def obter_tarefas(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    stmt = select(TarefaDB).offset(skip).limit(limit)
    tarefas = session.execute(stmt).scalars().all()
    return {'tarefas': tarefas}

@router.get('/{id}', response_model=Tarefa)
def obter_tarefa_por_id(id: int, session: Session = Depends(get_session)):
    tarefa = session.get(TarefaDB, id)
    
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    return tarefa

@router.put('/{id}', response_model=Tarefa)
def atualizar_tarefa(id: int,tarefa: Tarefa, session: Session = Depends(get_session), usuario_atual: UsuarioDB = Depends(obter_usuario_atual),):
    
    tarefa_atual = session.get(TarefaDB, id)
    
    if tarefa_atual is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa_atual.titulo=tarefa.titulo
    tarefa_atual.descricao=tarefa.descricao
    tarefa_atual.estado=tarefa.estado
    tarefa_atual.data_atualizacao=datetime.datetime.now()

    session.commit()
    session.refresh(tarefa_atual)
    return tarefa_atual

@router.delete('/{id}', response_model=Tarefa)
def deletar_tarefa_por_id(id: int, session: Session = Depends(get_session), usuario_atual: UsuarioDB = Depends(obter_usuario_atual)):
    tarefa = session.get(TarefaDB, id)
    
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    session.delete(tarefa)
    session.commit()
    return tarefa