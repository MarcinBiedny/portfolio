import logging
import logging.config
import logging.handlers
from app.extensions.logging.filters.level_filter import LevelFilter
from os import getenv


DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DEFAULT_LOG_DATEFMT = "%Y-%m-%d %H:%M%S"


def configure():
    log_dir = getenv("LOG_DIR")
    logging.config.dictConfig(
        {
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
                    "filename": f"{log_dir}/debug.log",
                    "filters": ["debug_filter"],
                },
                "info_file_handler": {
                    "class": "logging.FileHandler",
                    "formatter": "default",
                    "level": "INFO",
                    "filename": f"{log_dir}/info.log",
                    "filters": ["info_filter"],
                },
                "warning_file_handler": {
                    "class": "logging.FileHandler",
                    "formatter": "default",
                    "level": "WARNING",
                    "filename": f"{log_dir}/warning.log",
                    "filters": ["warning_filter"],
                },
                "error_file_handler": {
                    "class": "logging.FileHandler",
                    "formatter": "default",
                    "level": "ERROR",
                    "filename": f"{log_dir}/error.log",
                    "filters": ["error_filter"],
                },
                "critical_file_handler": {
                    "class": "logging.FileHandler",
                    "formatter": "default",
                    "level": "CRITICAL",
                    "filename": f"{log_dir}/critical.log",
                    "filters": ["critical_filter"],
                },
            },
            "loggers": {
                "": {  # root logger
                    "handlers": [
                        "console",
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
    )
