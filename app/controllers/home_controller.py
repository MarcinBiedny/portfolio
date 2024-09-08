from flask import render_template
from app.models.user_model import User


def index():
    user = User().query.first()

    return render_template("home.html", name=user.getName())
