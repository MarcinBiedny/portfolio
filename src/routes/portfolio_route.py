from flask import Blueprint
from src.controllers import portfolio_controller

bp = Blueprint('portfolio', __name__)

@bp.route('/portfolio/', methods=['GET'])
def route():
    return portfolio_controller.index()
