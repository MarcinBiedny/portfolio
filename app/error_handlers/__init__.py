# Script handling error handlers registration with 'app'
from flask import Flask
from app.error_handlers.page_not_found import handle as handle_404


def register_error_handlers(app: Flask):
    app.register_error_handler(404, handle_404)
