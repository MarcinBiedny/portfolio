from flask import render_template
from werkzeug.exceptions import NotFound


def handle(e: NotFound):
    return render_template("404.html")
