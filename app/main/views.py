from . import main
from flask import render_template, redirect, url_for
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
        password = reg_form.password.data
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
        
    return render_template('signup.html', form=reg_form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    #login if validation is successful
    if login_form.validate_on_submit():
        return "logged in!"

    return render_template('login.html', form=login_form)
