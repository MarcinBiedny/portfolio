# Script handling Bluepronts registration with 'app'
from flask import Flask
from app.routes import (
    home_route,
    projects_route,
    contact_route,
    login_route,
    logout_route,
)


def register_blueprints(app: Flask):
    app.register_blueprint(home_route.bp)
    app.register_blueprint(projects_route.bp)
    app.register_blueprint(contact_route.bp)
    app.register_blueprint(login_route.bp)
    app.register_blueprint(logout_route.bp)
