from http import HTTPStatus

from fastapi import FastAPI

from to_do_list.routers import autenticacao, tarefas
from to_do_list.schemas import Message

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")



app.include_router(autenticacao.router)
app.include_router(tarefas.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
