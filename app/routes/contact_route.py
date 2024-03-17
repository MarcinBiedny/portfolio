from flask import Blueprint
from app.controllers import contact_controller

bp = Blueprint("contact", __name__)


@bp.route("/contact/", methods=["GET"])
def route():
    return contact_controller.index()
