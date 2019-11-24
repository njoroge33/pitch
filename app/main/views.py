from . import main
from flask import render_template
from .forms import *
from ..models import *

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/signup' , methods=['GET', 'POST'])
def signup():
    reg_form = RegistrationForm()
    # if reg_form.validate_on_submit():
    #     username = reg_form.username.data
    #     password = reg_form.password.data

    #     #Check if username exists
    #     user_object = User.query.filter_by(username=username).first()
    #     if user_object:
    #         return "username already taken!"
        
    #     user = User(username=username, password=password)
    #     db.session.add(user)
    #     db.session.commit()
    #     return 'inserted into db!'


    return render_template('signup.html', form=reg_form)