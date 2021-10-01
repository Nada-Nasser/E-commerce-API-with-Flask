from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(label='User Name: ', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email Address:', validators=[DataRequired(), Length(max=50), Email()])
    password1 = PasswordField(label="Password:", validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField(label="Password Confirmation", validators=[EqualTo("password1"), DataRequired()])
    submit_button = SubmitField(label="Register")

