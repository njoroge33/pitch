from . import main
from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash
from flask_login import login_user, current_user, login_required, logout_user
from .forms import *
from ..models import *
from .. import db,photos
import arrow

@main.route('/')
def index():

    pitches = Pitch.query.all()
    return render_template('index.html', pitches=pitches)


@main.route('/signup' , methods=['GET', 'POST'])
def signup():

    reg_form = RegistrationForm()

    #updates the db if the validation was successful
    if reg_form.validate_on_submit():
        email = reg_form.email.data
        username = reg_form.username.data
        password = generate_password_hash(reg_form.password.data)
        
        user = User(email=email, username=username, password=password)
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
    form = PitchForm()

    if not current_user.is_authenticated:
        flash('please login', 'danger')
        return redirect(url_for('main.login'))

    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        description = form.description.data
        
        pitch = Pitch(owner_id=user.id, title=title, category=category, description=description)
        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('main.profile', uname=user.username))

    return render_template("profile.html", user=user, form=form)

@main.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('you have logged out successfuly', 'success')

    return redirect(url_for('main.index'))

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
