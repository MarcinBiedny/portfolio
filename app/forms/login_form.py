from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    MAX_USERNAME_LENGTH = 80
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 24

    username = StringField(
        label=f"Username (max {MAX_USERNAME_LENGTH} characters)",
        render_kw={
            "class": "form-control",
            "size": 2,
        },
        validators=[
            InputRequired(message="Username is required."),
            Length(max=MAX_USERNAME_LENGTH),
        ],
    )

    password = PasswordField(
        label=f"Password ({MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH} characters)",
        render_kw={
            "class": "form-control",
            "size": 2,
        },
        validators=[
            InputRequired(message="Password is required."),
            Length(
                min=MIN_PASSWORD_LENGTH,
                max=MAX_PASSWORD_LENGTH,
                message="Password must be between 8 and 24 characters.",
            ),
        ],
    )

    submit = SubmitField(label="Login", render_kw={"class": "btn btn-primary"})
