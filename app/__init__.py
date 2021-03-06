from flask import Flask
from config import config_options

#configurations for the database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#configuration for bootstrap
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
   app = Flask(__name__)   

   #create app configurations
   app.config.from_object(config_options[config_name])
   
   # Initializing flask extensions
   db.init_app(app)
   bootstrap.init_app(app)
   
   #Register the blueprint
   from .main import main as main_blueprint 
   app.register_blueprint(main_blueprint)

   return app 