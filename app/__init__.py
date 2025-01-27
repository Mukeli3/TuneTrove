#!/usr/bin/python3

import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


load_dotenv()
db = SQLAlchemy() #instantiate SQLAlchemy
login_manager = LoginManager()
jwt = JWTManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    """
    create and configure flask app
    """
    app = Flask(__name__, static_folder='static')

    app.config.from_object('app.config.Config')
    db.init_app(app) # initialize SQLAlchemy with the app
    jwt.init_app(app) # JWT with app

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    migrate = Migrate(app, db) # initialize flask_migrate

    # Register blueprints (routes)
    from app.routes.auth import auth
    from app.routes.recommendation_route import recom_bp
    from app.routes.search_route import search_bp
    from app.routes.spotify_route import spotify_bp

    app.register_blueprint(auth)
    app.register_blueprint(recom_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(spotify_bp)

    with app.app_context():
        from app.models import User, Recommendations, Song
        db.create_all() # creating db tables

    return app
