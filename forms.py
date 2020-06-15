from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators

class RegistrationForm(FlaskForm):
        username = StringField('Username', validators=[validators.DataRequired(), validators.Length(min=3, max=20)])
        email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
        password = PasswordField('Password', validators=[validators.DataRequired()])
        confirm_password = PasswordField('Confirm Password', validators=[validators.DataRequired(), validators.EqualTo('password')])
        submit = SubmitField('Submit')