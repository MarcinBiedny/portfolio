# Script handling extensions initialization with 'app'
from flask import Flask
from app.extensions.flask_sqlalchemy import db
from app.extensions.flask_migrate import migrate
from app.extensions.flask_restx import api_v1
from app.extensions.flask_wtf import csrf


def initialize_extensions(current_app: Flask):
    db.init_app(app=current_app)
    migrate.init_app(app=current_app, db=db)
    api_v1.init_app(app=current_app)
    csrf.init_app(app=current_app)
