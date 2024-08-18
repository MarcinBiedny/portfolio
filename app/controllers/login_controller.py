from flask import render_template, request, redirect, url_for, flash
from app.models.user_model import User
from app.forms.login_form import LoginForm
from app.forms.login_init_form import LoginInitForm
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import login_user


def index():
    init_user = User.query.first() is None

    form = _get_form(init_user)

    if form.validate_on_submit():
        if init_user:
            user = User(
                username=form.data["username"],
                password=generate_password_hash(form.data["password"]),
                name=form.data["first_name"],
                last_name=form.data["last_name"],
                email=form["email"],
            )
            user.save()
            login_user(user)
            flash("User created successfully. You can login now.", "success")
            return redirect(url_for("home.route"))
        else:
            user = User.query.filter_by(username=form.data["username"]).first()

        if user and check_password_hash(user.password, form.data["password"]):
            login_user(user)
            return redirect(url_for("home.route"))
        else:
            flash("Invalid username or password.", "error")
            return redirect(url_for("login.route"))

    return render_template(_get_template(init_user), form=form)


def _get_form(init_user: bool):
    if init_user:
        return LoginInitForm(request.form)

    return LoginForm(request.form)


def _get_template(init_user: bool):
    if init_user:
        return "login/login_init.html"

    return "login/login.html"
