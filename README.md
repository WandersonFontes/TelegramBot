# :robot: Telegram Bot
>Esse é uma API envio de mensagens no Telegram com DRF, Celery e RabbitMq

### [:world_map: Clique aqui e saiba mais sobre o projeto!](https://lapis-request-c58.notion.site/Telegram-Bot-d6509a8d5f414fdaab10a2bffd4327b3)

## Siga os seguintes passos para exeutar o projeto:

:one: Criar e ativar o ambiente virtual.
```console
# Criar 
python -m venv .venv
# Ativar
source .venv/bin/activate
```
:two: Instalar das bibliotecas.
```console
python -m pip install -r requirements.txt
```
:three: Preaparar a base de dados.
```console
python manage.py makemigrations
python manage.py migrate
```
:four: Executar o servidor local.
```console
python manage.py runserver
```
:five: Acessar a página root da API.

http://127.0.0.1:8000/api/v1/
>em caso de erro http://127.0.0.1:####/api/v1/ confira a porta no termial e corriga no navegador e tente novamente!

## Observações
>É necessário que você tenha o RabbitMQ instalado na máquina para que todos processos sejam executadas com sucesso!

### Execute o seguinte comando dentro do diretório do projeto:
>No mesmo diretório que for executado o comando para ativar servidor local.
```console
celery -A bot worker -l info -P solo
```


