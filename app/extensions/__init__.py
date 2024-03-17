# Script handling extensions initialization with 'app'
from flask import Flask
from app.extensions.flask_sqlalchemy import db
from app.extensions.flask_migrate import migrate


def initialize_extensions(current_app: Flask):
    db.init_app(app=current_app)
    migrate.init_app(app=current_app, db=db)
