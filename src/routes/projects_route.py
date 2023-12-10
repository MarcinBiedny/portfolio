from flask import Blueprint
from src.controllers import projects_controller

bp = Blueprint('projects', __name__)

@bp.route('/projects/', methods=['GET'], defaults={'project_name': None})
@bp.route('/projects/<project_name>/index.html', methods=['GET'])
def route(project_name):
    return projects_controller.index(project_name)
