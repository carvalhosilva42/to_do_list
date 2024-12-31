from fastapi import FastAPI
from http import HTTPStatus
from to_do_list.schemas import Tarefa, TarefaPublic, TarefaList
app = FastAPI()

@app.post('/tarefa/', status_code = HTTPStatus.CREATED, response_model=TarefaPublic)
def adiciona_tarefa(tarefa: Tarefa):
    return tarefa
'''
@app.get('/users/',reponse_model = TarefaList)
def obter_tarefas():
    return {'tarefas': []}'''