from fastapi import APIRouter
from http import HTTPStatus
import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from to_do_list.security import obter_senha_hash, verificar_senha, criar_acess_token, obter_usuario_atual

from to_do_list.database import get_session
from to_do_list.models import  UsuarioDB
from to_do_list.schemas import UsuarioList, Usuario, UsuarioPublic, Token
from to_do_list.security import (
    obter_usuario_atual,
    obter_senha_hash,
)

router = APIRouter(prefix='/usuario', tags=['usuarios'])


@router.post('/', status_code = HTTPStatus.CREATED, response_model=UsuarioPublic)
def adiciona_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    senha_encriptada = obter_senha_hash(usuario.senha)
    db_usuario = UsuarioDB(
        email=usuario.email,
        senha=senha_encriptada
        )
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario

@router.get('/', response_model=UsuarioList)
def obter_usuarios(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    stmt = select(UsuarioDB).offset(skip).limit(limit)
    usuarios = session.execute(stmt).scalars().all()
    return {'usuarios': usuarios}

@router.get('/{id}', response_model=Usuario)
def obter_usuario_por_id(id: int, session: Session = Depends(get_session)):
    usuario = session.get(UsuarioDB, id)
    
    if usuario is None:
        raise HTTPException(status_code=404, detail="usuario não encontrada")
    
    return usuario

@router.put('/{id}', response_model=Usuario)
def atualizar_usuario(id: int, usuario: Usuario, session: Session = Depends(get_session), usuario_atual: UsuarioDB = Depends(obter_usuario_atual)):
    
    if usuario_atual.id != id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Sem permissões suficientes'
        )
    usuario_atual.email=usuario.email
    usuario_atual.senha=obter_senha_hash(usuario.senha)

    session.commit()
    session.refresh(usuario_atual)
    return usuario_atual

@router.delete('/{id}', response_model=Usuario)
def deletar_usuario_por_id(id: int, session: Session = Depends(get_session), usuario_atual: UsuarioDB = Depends(obter_usuario_atual)):
    usuario = session.get(UsuarioDB, id)
    
    if usuario is None:
        raise HTTPException(status_code=404, detail="usuario não encontrada")
    session.delete(usuario)
    session.commit()
    return usuario



@router.post('/token/', response_model=Token)
def login_para_token_de_acesso(form_data: OAuth2PasswordRequestForm = Depends(),session: Session = Depends(get_session)):
    usuario = session.query(UsuarioDB).filter(UsuarioDB.email == form_data.username).first()
    if not usuario:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="E-mail incorreto"
        )
    if not verificar_senha(form_data.password,usuario.senha):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="E-mail ou senha incorreto"
        )
    
    token_acesso = criar_acess_token(data={'sub': usuario.email})

    return {'access_token': token_acesso, 'token_type': 'bearer'}