#!/usr/bin/python3
from flask import Blueprint, render_template, request, jsonify, make_response
from flask import current_app, session, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.utils.jwt_helper import generate_token, decode_token
from app.utils.bcrypt_helper import hash_password, verify_password
from app.models.user_model import User
from datetime import datetime, timedelta

auth = Blueprint('auth', __name__)

@auth.route("/")
def index():
    return render_template('index.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if not name or not email or not password:
            return jsonify({'message': 'All fields are required'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        hashed_password = hash_password(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        token = generate_token(email, secret_key=current_app.config['SECRET_KEY'])
        session['token'] = token

        return jsonify({'message': 'User registered successfully', 'token': token}), 201

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Login attempt: {email}, {password}")

        if not all([email, password]):
            return jsonify({'error': 'Email and password are required'}), 400

        # Find user in database
        user = User.query.filter_by(email=email).first()
        if not user or not verify_password(password, user.password):
            return jsonify({'error': 'Invalid credentials'}), 401

        token = create_access_token(identity=user.emaili)

        return jsonify({'token': token}), 200

@auth.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()

    print(f"JWT Token: {token}")
    print(f"JWT Token for current user: {current_user}")

    return render_template('home.html', user=current_user)
@auth.route('/logout', methods=['POST'])
def logout():
    # Clear the JWT token from the cookies
    response = make_response(jsonify({'message': 'Logged out successfully'}))
    response.delete_cookie('jwt')

    return response

@auth.route('/protected', methods=['GET'])
def protected():
    token = request.cookies.get('jwt')
    if not token:
        return jsonify({'error': 'Unauthorized'}), 401

    user_id = decode_token(token, SECRET_KEY)
    if isinstance(user_id, tuple):  # Handle errors from `decode_token`
        return user_id

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'message': f'Welcome, {user.name}!'}), 200
