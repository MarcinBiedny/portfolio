from flask import Flask
from src.routes import home_route

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_route.bp)
    return app
