from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from to_do_list.settings import Settings

# Criar o engine e a factory de sessões
engine = create_engine(Settings().DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função de dependência para obter uma sessão
def get_session():
    db = SessionLocal()
    try:
        yield db  # A sessão será gerida corretamente com o FastAPI
    finally:
        db.close()  # Fechar a sessão após o uso
