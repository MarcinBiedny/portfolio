from flask import Flask, render_template
from src.extensions.flask_sqlalchemy import (
    init_app as db_init_app,
    SQLALCHEMY_DATABASE_URI,
)
from src.extensions.flask_migrate import init_app as migrate_init_app
from src.routes import home_route, projects_route, contact_route

app = Flask(__name__)


def create_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

    initialize_extensions(app)

    app.register_blueprint(home_route.bp)
    app.register_blueprint(projects_route.bp)
    app.register_blueprint(contact_route.bp)

    return app


def initialize_extensions(app):
    db_init_app(app)
    migrate_init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
