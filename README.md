# :robot: Telegram Bot
>Esse foi um desafio propsto para a vaga de Desenvolvedor Python

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
>Consideramos que você tenha o RabbitMQ instalado na máquina para que o processo de consulta de usuário e o envio de mensagens seja gerenciado por e acompanhado por essa ferramenta.


