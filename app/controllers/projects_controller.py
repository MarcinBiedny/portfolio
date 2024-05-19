from flask import render_template
from app.models.project_model import Project


def index():
    return render_template("projects.html", projects=Project().get_all())
