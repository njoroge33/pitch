from . import main
from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from flask_login import login_user, current_user, login_required, logout_user
from .forms import *
from ..models import *

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/signup' , methods=['GET', 'POST'])
def signup():

    reg_form = RegistrationForm()

    #updates the db if the validation was successful
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = generate_password_hash(reg_form.password.data)
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        flash('Registered successfully.Please login', 'success')

        return redirect(url_for('main.login'))
        
    return render_template('signup.html', form=reg_form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    #login if validation is successful
    if login_form.validate_on_submit():

        user_object =User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('main.profile',uname=login_form.username.data))
        

    return render_template('login.html', form=login_form)


@main.route('/user/<uname>', methods=['GET', 'POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if not current_user.is_authenticated:
        flash('please login', 'danger')
        return redirect(url_for('main.login'))

    return render_template("profile.html", user = user)

@main.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('you have logged out successfuly', 'success')

    return redirect(url_for('main.login'))
