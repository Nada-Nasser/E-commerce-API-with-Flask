from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from market import app, db
from market.forms import RegistrationForm, LoginForm
from market.models import Item, User


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("home.html")


@app.route('/market')
@login_required
def market():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.username.data,
                    email_address=form.email.data,
                    password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f"The account is created and you logged in successfully as {form.username.data}", category="success")
        return redirect(url_for("market"))

    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f"There is an error : {error_msg}" , category="danger")

    return render_template("register_form.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    attempted_user = User.query.filter_by(name=form.username.data).first()
    if form.validate_on_submit():
        if attempted_user and attempted_user.check_password_correction(form.password.data):
            login_user(attempted_user)
            flash(f"You logged in successfully as {form.username.data}", category="success")
            return redirect(url_for("market"))
        else:
            flash(f"The email and password does not match, Try new ones", category="danger")
    return render_template("login_form.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out!", category="info")
    return redirect(url_for("homepage"))
    
    