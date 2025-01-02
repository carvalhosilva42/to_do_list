FROM python:3.11-slim
ENV POETRY_VIRTUALENVS_CREATE=false

# Define o diretório de trabalho
WORKDIR /app

# Copia todos os arquivos para o contêiner
COPY . .

# Instala o Poetry
RUN pip install poetry

# Configura o Poetry e instala as dependências
RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

# Expõe a porta do servidor
EXPOSE 8000

# Define o comando para rodar as migrações do Alembic antes de iniciar o servidor
CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run uvicorn --host 0.0.0.0 to_do_list.app:app"]

