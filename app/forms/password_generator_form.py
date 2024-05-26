from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from app.services.password_generator import PasswordGenerator


class PasswordGeneratorForm(FlaskForm):
    password_length = IntegerField(
        label="Password length",
        default=24,
        validators=[
            InputRequired(),
            NumberRange(
                min=PasswordGenerator.MINIMUM_PASSWORD_LEN,
                max=PasswordGenerator.MAXIMUM_PASSWORD_LEN,
                message=(
                    "Password lenght must be between {PasswordGenerator.MINIMUM_PASSWORD_LEN}"
                    "and {PasswordGenerator.MAXIMUM_PASSWORD_LEN}"
                ),
            ),
        ],
        render_kw={
            "class": "form-control",
            "size": 2,
        },
    )
    include_uppercase = BooleanField(
        label="Include uppercase letters",
        render_kw={"class": "form-check-input"},
    )
    include_numbers = BooleanField(
        label="Include digits",
        render_kw={"class": "form-check-input"},
    )
    include_special_chars = BooleanField(
        label="Include special characters",
        render_kw={"class": "form-check-input"},
    )
    submit = SubmitField(label="Generate", render_kw={"class": "btn btn-primary"})
