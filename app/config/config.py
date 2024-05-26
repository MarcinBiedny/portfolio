from os import getenv


class Config(object):
    SECRET_KEY = getenv("SECRET_KEY")
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"{getenv('SQLALCHEMY_DATABASE_SYSTEM')}+"
        f"{getenv('SQLALCHEMY_DATABASE_DRIVER')}://"
        f"{getenv('MYSQL_USER')}:"
        f"{getenv('MYSQL_PASSWORD')}@"
        f"{getenv('SQLALCHEMY_DATABASE_HOST')}:"
        f"{getenv('SQLALCHEMY_DATABASE_PORT')}/"
        f"{getenv('MYSQL_DATABASE')}"
    )

    # flask_json
    # https://flask-json.readthedocs.io/en/latest/
    JSON_ADD_STATUS = False
