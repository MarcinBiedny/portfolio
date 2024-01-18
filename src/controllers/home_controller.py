from flask import render_template
from src.models.user_model import User


def index():
    user = User().query.filter_by(id=1).first()
    name = "Anonymous" if user == None else user.getName()

    return render_template("home.html", name=name)
