from flask_migrate import Migrate
from src.extensions.flask_sqlalchemy import db

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
