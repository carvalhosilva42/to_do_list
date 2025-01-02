# to_do_list
Um desafio para a vaga de desenvolvedor backend python

Informações para Executar o Ambiente:

(1) git clone https://github.com/carvalhosilva42/to_do_list.git
(2) docker build -t "to_do_list" .
(3) docker run -v $(pwd)/db.sqlite3:/app/db.sqlite3 -p 8000:8000 to_do_list
