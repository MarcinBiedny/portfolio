from flask import Blueprint
from src.controllers import projects_controller
from src.models.project_model import Project

bp = Blueprint('projects', __name__)

@bp.route('/projects/', methods=['GET'], defaults={'project_name': None})
@bp.route('/projects/<project_name>/index.html', methods=['GET'])
def route(project_name):
    projects = [] if not project_name is None else Project().get_all()

    return projects_controller.index(project_name, projects)
