from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class EstadoTarefa(str, Enum):
    pendente = "pendente"
    em_andamento = "em andamento"
    concluido = "concluido"

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    estado: EstadoTarefa = Field(default=EstadoTarefa.pendente)
    data_criacao: datetime = Field(default_factory=datetime.now)
    data_atualizacao: datetime = Field(default_factory=datetime.now)

class TarefaPublic(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class TarefaList(BaseModel):
    tarefas: list[Tarefa]