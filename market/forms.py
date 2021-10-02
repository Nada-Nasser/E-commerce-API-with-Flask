from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from market.models import User


class RegistrationForm(FlaskForm):
    def validate_username(self, name_to_be_checked):
        user = User.query.filter_by(name=name_to_be_checked.data).first()
        if user:
            raise ValidationError("This username is already exists, try to use other username")

    def validate_email(self, email_to_be_checked):
        user = User.query.filter_by(email_address=email_to_be_checked.data).first()
        if user:
            raise ValidationError("This email address is already exists, try to use other email address")

    username = StringField(label='User Name: ', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email Address:', validators=[DataRequired(), Length(max=50), Email()])
    password1 = PasswordField(label="Password:", validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField(label="Password Confirmation", validators=[EqualTo("password1"), DataRequired()])
    submit_button = SubmitField(label="Register")


class LoginForm(FlaskForm):
    username = StringField(label='User Name: ', validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField(label="Password:", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField(label="Login")


class PurchaseForm(FlaskForm):
    submit = SubmitField(label="Purchase")


class SellForm(FlaskForm):
    submit = SubmitField(label="Sell")

