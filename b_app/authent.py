from flask import Blueprint, render_template, redirect, url_for
from flask import request, flash, current_user
from b_app import app, db, bcrypt
from b_app.models import User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

# handle user authentication
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            flash('Please confirm your credentials. Login unsuccessful', 'danger')
        return render_template('index.html')

@auth.route('/register', method=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('profile'))
    return render_template('index.html')

@auth.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current.use.username)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
