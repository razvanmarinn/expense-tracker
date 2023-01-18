from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, login_required
from website.models import TransferModel

views = Blueprint('views', __name__)

transfer_model = TransferModel()

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated:
        data = transfer_model.get_all_transfers()
        print(data)
        return render_template('dashboard.html', data=data, user=current_user)

@views.route('/approve_transfer/', methods=['POST'])
def my_link():
    transfer_id = request.json['transfer_id']
    return jsonify(transfer_model.approve_the_transfer(transfer_id))
