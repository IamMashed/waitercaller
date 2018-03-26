from flask_wtf import Form
from wtforms import PasswordField
from wtforms import SubmitField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(Form):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'password',
        validators=[
            DataRequired(),
            Length(
                min=8,
                message="Please choose a password of at least 8 characters")
        ])
    password2 = PasswordField(
        'password2',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match')
        ])
    submit = SubmitField('submit', validators=[DataRequired()])


class LoginForm(Form):
    loginemail = EmailField('email', validators=[DataRequired(), Email()])
    loginpassword = PasswordField(
        'password',
        validators=[DataRequired(message="Password field is required")])
    submit = SubmitField('submit', [DataRequired()])


class CreateTableForm(Form):
	tablenumber = TextField('tablenumber', validators=[DataRequired()])
	submit = SubmitField('createtablesubmit', validators=[DataRequired()])