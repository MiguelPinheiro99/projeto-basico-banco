# projeto-basico-banco
Meu primeiro projeto de programação, nele eu testei de forma simples as ferramentas que venho estudando ultimamente (python, django, mysql, consumo de API e git), é um projeto simples que simula algumas funções de um banco

## Recursos

- Criação de contas bancárias
- Exibição de detalhes da conta
- Depósitos e saques
- Transferências entre contas
- Conversão de moedas com base na taxa de câmbio atual que é disponibilizada por uma API

## Tecnologias

- Django
- MySQL
- API de taxa de câmbio

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados:**

    Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

    ```env
    SECRET_KEY='sua-chave-secreta'
    DEBUG=True
    DB_NAME='nome_do_banco'
    DB_USER='seu_usuario'
    DB_PASSWORD='sua_senha'
    DB_HOST='localhost'
    DB_PORT='3306'
    API_KEY='sua_api_key'
    ```

5. **Aplique as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

6. **Inicie o servidor:**

    ```bash
    python manage.py runserver
    ```

    Acesse o projeto em `http://127.0.0.1:8000/`.

## Uso

O sistema é bem intuitivo, cada página realiza uma função

