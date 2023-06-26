from flask import Blueprint, render_template, redirect, url_for, request
from .forms import RegisterForm, LoginForm
from ..models import User
from flask_login import current_user, login_user, logout_user, login_required, user_logged_in
from app import app

# establishes the auth branch to route to the webpages in the auth template folder 
auth = Blueprint('auth', __name__, template_folder="auth_templates")

@auth.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('search'))
    form = RegisterForm()
    print(request.method)
    if request.method == "POST":
        if form.validate():
            name = form.name.data.title()
            username = form.username.data.lower()
            password = form.password.data
            email = form.email.data.lower()
            print("Account created!")

            user = User(name, username, email, password)
            user.save_user()

            return(redirect(url_for('auth.login')))



    return render_template('register.html', register_form=form)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('search'))
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            print("working!")
            # user_name = form.username.data
            entry = form.entry.data.lower()
            password = form.password.data
            # check user's entry against email and username
            username_check = User.query.filter_by(username=entry).first()
            email_check = User.query.filter_by(email=entry).first()
            # user = email or username depending on which value was entered
            if username_check:
                user = username_check
            if email_check:
                user = email_check
            if username_check or email_check:
                if user.password == password:
                    print("Logged in successfully")
                    login_user(user)
                    return(redirect(url_for('dashboard')))
                else:
                    print("Wrong Password entered. Please try again")
            else:
                print("There is no user with this username or email. Please register an account")

    return render_template('login.html', login_form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))