from flask_sqlalchemy import SQLAlchemy
from os import getenv


SQLALCHEMY_DATABASE_URI = (
    f"{getenv('SQLALCHEMY_DATABASE_SYSTEM')}+"
    f"{getenv('SQLALCHEMY_DATABASE_DRIVER')}://"
    f"{getenv('MYSQL_USER')}:"
    f"{getenv('MYSQL_PASSWORD')}@"
    f"{getenv('SQLALCHEMY_DATABASE_HOST')}:"
    f"{getenv('SQLALCHEMY_DATABASE_PORT')}/"
    f"{getenv('MYSQL_DATABASE')}"
)

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
