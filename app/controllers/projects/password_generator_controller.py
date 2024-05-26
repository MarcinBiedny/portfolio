from flask import render_template, url_for, request
from app.services.password_generator import PasswordGenerator
from app.forms.password_generator_form import PasswordGeneratorForm


def index():
    form = PasswordGeneratorForm(request.form)
    password = ""

    if form.validate_on_submit():
        form_data = request.form.to_dict()
        password = PasswordGenerator().generate(
            include_uppercase=bool(form_data.get(form.include_uppercase.name, False)),
            include_numbers=bool(form_data.get(form.include_numbers.name, False)),
            include_special_chars=bool(
                form_data.get(form.include_special_chars.name, False)
            ),
            password_length=int(form_data.get(form.password_length.name, 24)),
        )

    return render_template(
        url_for("projects.password_generator_index"), form=form, password=password
    )
