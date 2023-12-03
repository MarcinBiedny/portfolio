from flask import render_template

def index(project_name, projects):
    template = 'projects.html' if project_name is None else f'projects/{project_name}/index.html'

    return render_template(template, projects=projects)
