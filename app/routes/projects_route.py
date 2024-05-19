from flask import Blueprint
from app.controllers import projects_controller
from app.controllers.projects import calculator_controller
from app.controllers.projects import password_generator_controller

bp = Blueprint("projects", __name__)


@bp.route("/projects/", methods=["GET"])
def index():
    return projects_controller.index()


@bp.route("/projects/calculator/index.html", methods=["GET"])
def calculator_index():
    return calculator_controller.index()


@bp.route("/projects/password-generator/index.html", methods=["GET", "POST"])
def password_generator_index():
    return password_generator_controller.index()
