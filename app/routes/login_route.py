from flask import Blueprint
from app.controllers import login_controller

bp = Blueprint("login", __name__)


@bp.route("/login/", methods=["GET", "POST"])
def route():
    return login_controller.index()
