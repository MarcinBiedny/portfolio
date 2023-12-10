from flask import render_template, redirect, url_for
from jinja2 import TemplateNotFound
from src.models.project_model import Project

MAIN_PROJECTS_TEMPLATE = "projects.html"


def index(project_name):
    template = MAIN_PROJECTS_TEMPLATE if project_name is None else f'projects/{project_name}/index.html'
    projects = (Project().get_all()) if (template == MAIN_PROJECTS_TEMPLATE) else None

    try:
        return render_template(template, projects=projects)
    except TemplateNotFound:
        return redirect(url_for('projects.route', project_name=None))
