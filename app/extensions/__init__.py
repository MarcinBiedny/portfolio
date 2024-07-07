# Script handling extensions initialization with 'app'
from flask import Flask
from app.extensions import logging
from app.extensions.flask_sqlalchemy import db
from app.extensions.flask_migrate import migrate
from app.extensions.flask_restx import api_v1
from app.extensions.flask_wtf import csrf
from app.extensions.flask_login import login_manager


def initialize_extensions(current_app: Flask):
    logging.init_app(app=current_app)
    db.init_app(app=current_app)
    migrate.init_app(app=current_app, db=db)
    api_v1.init_app(app=current_app)
    csrf.init_app(app=current_app)
    login_manager.init_app(app=current_app)
