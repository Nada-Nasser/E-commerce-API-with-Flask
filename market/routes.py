from flask import render_template, redirect, url_for

from market import app, db
from market.forms import RegistrationForm
from market.models import Item, User


@app.route('/')
def hello_world():
    return '<h1>hello World</h1>'


@app.route('/homepage')
def homepage():
    return render_template("home.html")


@app.route('/market')
def market():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route('/register',methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.username.data, email_address=form.email.data,hashed_password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("market"))

    if form.errors != {}:
        for error_msg in form.errors.values():
            print(f"There is an error : {error_msg}")
    return render_template("register_form.html", form=form)

