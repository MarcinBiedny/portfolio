from flask import Blueprint
from app.controllers import projects_controller
from app.controllers.projects import calculator_controller
from app.controllers.projects import password_generator_controller
from flask_login import login_required

bp = Blueprint("projects", __name__)


@bp.route("/projects/", methods=["GET"])
@login_required
def index():
    return projects_controller.index()


@bp.route("/projects/calculator/index.html", methods=["GET"])
@login_required
def calculator_index():
    return calculator_controller.index()


@bp.route("/projects/password-generator/index.html", methods=["GET", "POST"])
@login_required
def password_generator_index():
    return password_generator_controller.index()
