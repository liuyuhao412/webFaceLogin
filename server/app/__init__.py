from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    CORS(app,resources=r'/*')
    app.config.from_object(config[config_name])
    db.init_app(app)
    from .mainView import mainView as mainView_blueprint
    app.register_blueprint(mainView_blueprint)
    return app