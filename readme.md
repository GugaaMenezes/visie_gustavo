# Mini app

#### Exercício teste, contendo o cadastro de artigos em um mini app. 


### Backend 
- Python (3.11.3);
- Flask (3.0.0)
### Frontend
- HTML
- Javascript
- Bootstrap(5.3);
### Banco de Dados
- MySQL

### Dependências

- Flask(3.0.0);
- Flask-Cors(4.0.0);
- Flask-SQLAlchemy(3.1.1);
- mysqlclient(2.2.0);
- pytest(7.4.3);
- SQLAlchemy(2.0.21);
- Werkzeug(3.0.1);### Execução

1. Clone este repositório:

   ```
   git clone https://github.com/GugaaMenezes/visie_gustavo.git
   ```

2. Crie um ambiente virtual para testes (opcional):  
   ```
   python -m venv venv
   ```
2.1 Acesse o ambiente virtual:
   ```
   venv\Scripts\activate
   ```

3. Realize a instalação de todas as dependências, do arquivo **requirements.txt**:

   ```
   pip install -r requirements.txt
   ```

4. Edite o arquivo **config.ini** para adicionar a senha do banco de dados informado no email:

   ```
   [DATABASE]
    sgbd = mysql
    user = gustavomenezes
    passwd =  ; **insira aqui a senha do banco de dados **
    db = gustavomenezes
    host = jobs.visie.com.br
    port = 3306
    charset = utf8
    autocommit = False
   ```

5. Crie o banco de dados, juntamente com as tabelas pré-definidas:

   ```
   python manage.py migrate
   ```

5. Execute o servidor:

   ```
   python run.py
   ```


> *O **Frontend** está configurado para ser executado no endereço http://127.0.0.1:5000*.

> Modo debug segue ativado por padrão.


## Autores

- Gustavo Menezes - [@gugaamenezes](https://github.com/GugaaMenezes) 


## Funcionalidades

- Novos registros;
- Lista dos resgistros;
- Exclusão dos registros

