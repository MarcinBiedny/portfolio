# Script handling extensions initialization with 'app'
from flask import Flask
from src.extensions.flask_sqlalchemy import db
from src.extensions.flask_migrate import migrate


def initialize_extensions(current_app: Flask):
    db.init_app(app=current_app)
    migrate.init_app(app=current_app, db=db)
