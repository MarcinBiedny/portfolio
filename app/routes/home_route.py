from flask import Blueprint
from app.controllers import home_controller

bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"])
@bp.route("/home/", methods=["GET"])
def route():
    return home_controller.index()
