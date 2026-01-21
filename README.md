# README

1. Criando o venv

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. Alterando a viariavel de ambiente:
```
export FLASK_ENV=development
```
3. Executando a aplicação
```
python3 livro_flask/run.py
```

4. Crie o banco de dados que será utilizado:
```
sudo apt install mysql-server
sudo systemctl start mysql
sudo mysql_secure_installation  # Configurações de segurança

sudo mysql

CREATE DATABASE livro_flask CHARACTER SET UTF8 collate utf8_general_ci;

SHOW DATABASES;   #Checar o banco de dados
EXIT;     # Encerrando

# Criando o usuáriio (No liro não pediu)
CREATE USER 'flaskuser'@'localhost' IDENTIFIED BY 'senha123';
GRANT ALL PRIVILEGES ON livro_flask.* TO 'flaskuser'@'localhost';
FLUSH PRIVILEGES;


```
5. Instale os componentes necessários do python:

```
sudo apt-get install python3-dev libmysqlclient-dev
pip install mysqlclient
pip install flask-mysqldb 

# Caso os 2 ultimos comandos deem erro:
sudo apt update
sudo apt install -y pkg-config libmysqlclient-dev build-essential
```