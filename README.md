# to_do_list
Um desafio para a vaga de desenvolvedor backend python

Aplicação CRUD completa de tarefas de Lista to do. Campos

- id
- título
- descrição (opcional)
- estado ("pendente", "em andamento" ou "concluída")
- data_criação
- data_atualização

Endpoints para:

- Criar Tarefas (POST /tarefa/)
- Listar todas as tarefas (GET /tarefa/)
- Atualizar uma tarefa (PUT /tarefa/)
- Deletar uma tarefa (DELETE /tarefa/)
- Visualizar uma tarefa específica pelo ID (GET /tarefa/{id})

Os endpoints de atualização e exclusão de uma tarefa são protegidos com JWT. Portanto, é necessária a criação de um
usuário para geração do token. Endpoints para usuário:

- Criar usuário (POST /usuario/)
- Listar todos os usuários (GET /usuario/)
- Atualizar um usuário (PUT /usuario/)
- Deletar um usuário (DELETE /usuario/)
- Visualizar um usuário específico pelo ID (GET /usuario/{id})
- Criar token (POST /usuario/token/)

## Informações para executar localmente a aplicação

(1) git clone https://github.com/carvalhosilva42/to_do_list.git

(2) pip install poetry

(3) poetry config installer.max-workers 10

(4) poetry install --no-interaction --no-ansi



## Informações para Executar o Ambiente em Docker:

(1) git clone https://github.com/carvalhosilva42/to_do_list.git

(2) docker build -t "to_do_list" .

(3) docker run -v $(pwd)/db.sqlite3:/app/db.sqlite3 -p 8000:8000 to_do_list
