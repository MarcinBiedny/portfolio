from flask_login import LoginManager
from app.models.user_model import User
from app.routes.login_route import bp

login_manager = LoginManager()
login_manager.login_view = bp.name + ".route"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get({"id": int(user_id)})
