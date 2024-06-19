from flask import Flask
import logging.config


def init_app(app: Flask):
    logging.config.dictConfig(app.config["LOGGING"])
