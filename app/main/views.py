from . import main
from flask import render_template
from .forms import *

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/signup' , methods=['GET', 'POST'])
def signup():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        return 'great'
    return render_template('signup.html', form=reg_form)