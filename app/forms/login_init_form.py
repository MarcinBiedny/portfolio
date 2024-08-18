from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import InputRequired
from app.forms.login_form import LoginForm


class LoginInitForm(LoginForm):
    first_name = StringField(
        label="First Name",
        render_kw={"class": "form-control", "size": 2},
        validators=[InputRequired(message="First Name is required.")],
    )
    last_name = StringField(
        label="Last Name",
        render_kw={"class": "form-control", "size": 2},
        validators=[InputRequired(message="Last Name is required.")],
    )
    email = EmailField(
        label="Email",
        render_kw={"class": "form-control", "size": 2},
        validators=[InputRequired(message="Email is required.")],
    )
    submit = SubmitField(label="Create", render_kw={"class": "btn btn-primary"})
