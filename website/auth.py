from flask import Blueprint, render_template, request, redirect,url_for, current_app, flash
from flask_login import login_required, current_user , login_user, logout_user
from website.models import User, UserModel
import bcrypt
import time
import random

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_model = UserModel()
        user = user_model.get_user_by_username(username)
        if user is not None:
            User_object = User(user[0], user[1], user[2])
            if bcrypt.checkpw(password.encode('utf-8') , bytes(user[2] , 'utf-8')):
                time.sleep(2)
                login_user(User_object)
                return redirect((url_for('views.dashboard')))


            else:
                return render_template('login.html', error='Invalid username or password')
        else:
    # login failed
            flash('Invalid username or password', category = 'error')
    return render_template("login.html",  user=current_user)








@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))



@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        user_model = UserModel()
        user = user_model.get_user_by_username(username)
        if user is not None:
            return render_template('sign_up.html', error='Username already used')
        else:
            hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14)).decode('utf-8')
            new_user = User(random.randrange(1,99999), username, hashed_pass)
            user_model.create_user(new_user)
            return redirect((url_for('views.home')))

    return render_template('sign_up.html', error='Invalid username or password', user=current_user)




