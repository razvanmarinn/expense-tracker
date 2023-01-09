from flask import Blueprint, render_template
from flask_login import current_user, login_required


views = Blueprint('views', __name__)



@views.route('/')
def home():
    return render_template('home.html')



@views.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated:
        return render_template('dashboard.html', user=current_user)
