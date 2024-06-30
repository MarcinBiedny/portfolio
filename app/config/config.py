from os import getenv
import logging
from app.extensions.logging.filters.level_filter import LevelFilter


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

    # logging
    # https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
    DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DEFAULT_LOG_DATEFMT = "%Y-%m-%d %H:%M%S"
    LOG_DIR = getenv("LOG_DIR")
    APP_LOGGER_NAME = getenv("APP_LOGGER_NAME")

    LOGGING = {
        "version": 1,
        "formatters": {
            "default": {
                "format": DEFAULT_LOG_FORMAT,
                "datefmt": DEFAULT_LOG_DATEFMT,
            },
        },
        "filters": {
            "debug_filter": {"()": LevelFilter, "level": logging.DEBUG},
            "info_filter": {"()": LevelFilter, "level": logging.INFO},
            "warning_filter": {"()": LevelFilter, "level": logging.WARNING},
            "error_filter": {"()": LevelFilter, "level": logging.ERROR},
            "critical_filter": {"()": LevelFilter, "level": logging.CRITICAL},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": "DEBUG",
            },
            "debug_file_handler": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "level": "DEBUG",
                "filename": f"{LOG_DIR}/debug.log",
                "filters": ["debug_filter"],
            },
            "info_file_handler": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "level": "INFO",
                "filename": f"{LOG_DIR}/info.log",
                "filters": ["info_filter"],
            },
            "warning_file_handler": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "level": "WARNING",
                "filename": f"{LOG_DIR}/warning.log",
                "filters": ["warning_filter"],
            },
            "error_file_handler": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "level": "ERROR",
                "filename": f"{LOG_DIR}/error.log",
                "filters": ["error_filter"],
            },
            "critical_file_handler": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "level": "CRITICAL",
                "filename": f"{LOG_DIR}/critical.log",
                "filters": ["critical_filter"],
            },
        },
        "loggers": {
            "": {  # root logger
                "handlers": [
                    "console",
                ],
                "level": "DEBUG",
                "propagate": False,
            },
            APP_LOGGER_NAME: {
                "handlers": [
                    "debug_file_handler",
                    "info_file_handler",
                    "warning_file_handler",
                    "error_file_handler",
                    "critical_file_handler",
                ],
                "level": "DEBUG",
                "propagate": True,
            },
            "werkzeug": {
                "handlers": [
                    "debug_file_handler",
                    "info_file_handler",
                    "warning_file_handler",
                    "error_file_handler",
                    "critical_file_handler",
                ],
                "level": "DEBUG",
                "propagate": True,
            },
        },
    }
