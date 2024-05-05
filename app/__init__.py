from dotenv import load_dotenv

# Loading environment variables from '.env file
# before anu other code
load_dotenv()

from flask import Flask
from app.extensions import initialize_extensions
from app.routes import register_blueprints
from app.error_handlers import register_error_handlers


app = Flask(__name__)


def create_app(flask_env: str):
    app.config.from_object(f"app.config.{flask_env.title()}Config")

    register_error_handlers(app)
    register_blueprints(app)
    initialize_extensions(app)

    return app
