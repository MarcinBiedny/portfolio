from flask import render_template, request, redirect, url_for, flash
from app.models.user_model import User
from app.forms.login_form import LoginForm
from flask_bcrypt import check_password_hash
from flask_login import login_user


def index():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.data["username"]).first()

        if user and check_password_hash(user.password, form.data["password"]):
            login_user(user)
            return redirect(url_for("home.route"))
        else:
            flash("Invalid username or password.", "error")
            return redirect(url_for("login.route"))

    return render_template("login.html", form=form)
