from flask import Blueprint
from src.controllers import home_controller

bp = Blueprint('home', __name__)

@bp.route('/')
def route():
    return home_controller.index()
