from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class PokeForm(FlaskForm):
    pokemon = StringField("Pokemon", validators=[DataRequired()])
    submit = SubmitField()

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=18)])
    username = StringField("Username", validators=[DataRequired(), Length(min=6, max=18)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=24)])
    confirm_password = PasswordField("ConfirmPassword", validators=[DataRequired(), EqualTo("password")])
    email = EmailField("Email", validators=[DataRequired()])
    register = SubmitField()

class LoginForm(FlaskForm):
    # username = StringField("Username", validators=[DataRequired(), Length(min=6)])
    entry = StringField("Entry", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    login = SubmitField()

class CatchForm(FlaskForm):
    catch = SubmitField()