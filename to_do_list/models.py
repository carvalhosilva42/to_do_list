from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, registry, mapped_column

table_registry = registry()

@table_registry.mapped_as_dataclass
class TarefaDB:
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(init=False, primary_key= True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    estado: Mapped[str] = mapped_column(nullable=False)
    descricao: Mapped[str] = mapped_column(nullable=True, default=None)
    data_criacao: Mapped[datetime] = mapped_column(init=False,server_default=func.now())
    data_atualizacao: Mapped[datetime] = mapped_column(init=False,server_default=func.now())
