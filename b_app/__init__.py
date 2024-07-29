from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('b_app.config')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please login to access TuneTrove'

from b_app.authent import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from b_app.routes import routes as routes_blueprint
app.register_blueprint(routes_blueprint)

from b_app import models
