from flask import Blueprint
from app.controllers import projects_controller

bp = Blueprint("projects", __name__)


@bp.route("/projects/", methods=["GET"], defaults={"project_name": None})
@bp.route("/projects/<path:project_name>/index.html", methods=["GET"])
def route(project_name):
    return projects_controller.index(project_name)
