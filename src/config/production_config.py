from .config import Config


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "localhost://"
