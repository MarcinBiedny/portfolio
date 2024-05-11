import pytest
from flask import Flask


@pytest.fixture()
def app():
    from app import create_app

    app = create_app(flask_env="testing")
    with app.app_context():
        yield app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()


@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()
