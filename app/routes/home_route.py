from flask import Blueprint
from app.controllers import home_controller
from flask_login import login_required

bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"])
@bp.route("/home/", methods=["GET"])
@login_required
def route():
    return home_controller.index()
