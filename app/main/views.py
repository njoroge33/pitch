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

    #updates the db if the validation was successful
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return 'inserted into db!'
        
    return render_template('signup.html', form=reg_form)