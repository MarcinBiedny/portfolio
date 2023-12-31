from flask import Flask
from src.routes import home_route, projects_route, contact_route


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_route.bp)
    app.register_blueprint(projects_route.bp)
    app.register_blueprint(contact_route.bp)

    return app
