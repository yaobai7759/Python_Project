from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.__init__(app)
    return app,db

tool = create_app()


if __name__ == '__main__':
    tool[0].run()