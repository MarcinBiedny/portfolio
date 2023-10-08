from flask import render_template
from src.models import user_model

def index():
    return render_template('home.html', name=user_model.getName())
