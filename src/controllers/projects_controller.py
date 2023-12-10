from flask import render_template
from src.models.project_model import Project

MAIN_PROJECTS_TEMPLATE = "projects.html"


def index(project_name):
    template = MAIN_PROJECTS_TEMPLATE if project_name is None else f'projects/{project_name}/index.html'
    projects = (Project().get_all()) if (template == MAIN_PROJECTS_TEMPLATE) else None

    return render_template(template, projects=projects)
