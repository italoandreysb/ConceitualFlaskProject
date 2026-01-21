# -*- coding: utf-8 -*
from flask import Flask 

# config import
from config import app_config, app_active 
config = app_config[app_active] 

# módulos de conexão com o banco
from flask_sqlalchemy import SQLAlchemy 

def create_app(config_name):
   app = Flask(__name__, template_folder='templates')

   app.secret_key = config.SECRET
   app.config.from_object(app_config[config_name])
   app.config.from_pyfile('config.py')

   # Conexão com o banco
   app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI 
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
   db = SQLAlchemy(config.APP) 
   db.init_app(app) 


   @app.route('/')
   def index():
      return 'Oi, meu chapa!'

   return app