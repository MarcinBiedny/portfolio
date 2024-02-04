from flask import Flask
from src.extensions import initialize_extensions
from src.routes import register_blueprints
from src.error_handlers import register_error_handlers


app = Flask(__name__)


def create_app():
    initialize_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    return app
