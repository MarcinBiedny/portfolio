from flask_login import LoginManager
from app.models.user_model import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return None if user_id is None else User.query.get({"id": user_id})
