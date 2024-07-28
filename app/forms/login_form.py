from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        label="Username",
        render_kw={
            "class": "form-control",
            "size": 2,
        },
        validators=[InputRequired(message="Username is required.")],
    )

    password = PasswordField(
        label="Password",
        render_kw={
            "class": "form-control",
            "size": 2,
        },
        validators=[
            InputRequired(message="Password is required."),
            Length(
                min=8, max=24, message="Password must be between 8 and 24 characters."
            ),
        ],
    )

    login = SubmitField(label="Login", render_kw={"class": "btn btn-primary"})
