from flask import Blueprint
from app.controllers import contact_controller
from flask_login import login_required

bp = Blueprint("contact", __name__)


@bp.route("/contact/", methods=["GET"])
@login_required
def route():
    return contact_controller.index()
