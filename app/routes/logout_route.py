from flask import Blueprint, redirect, url_for
from flask_login import logout_user

bp = Blueprint("logout", __name__)


@bp.route("/logout/", methods=["GET", "POST"])
def route():
    logout_user()
    return redirect(url_for("login.route"))
