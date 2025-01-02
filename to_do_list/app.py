from http import HTTPStatus

from fastapi import FastAPI

from to_do_list.routers import autenticacao, tarefas
from to_do_list.schemas import Message

app = FastAPI()
app.include_router(autenticacao.router)
app.include_router(tarefas.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
