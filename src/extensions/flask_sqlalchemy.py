from flask_sqlalchemy import SQLAlchemy
from os import getenv


db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
