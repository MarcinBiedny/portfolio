# Script handling extensions initialization with 'app'
from flask import Flask
from src.extensions.flask_sqlalchemy import init_app as db_init_app
from src.extensions.flask_migrate import init_app as migrate_init_app


def initialize_extensions(app: Flask):
    db_init_app(app)
    migrate_init_app(app)
