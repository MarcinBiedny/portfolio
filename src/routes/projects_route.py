from flask import Blueprint
from src.controllers import projects_controller

bp = Blueprint('projects', __name__)

@bp.route('/projects/', methods=['GET'])
def route():
    return projects_controller.index()
