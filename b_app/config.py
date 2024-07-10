import os
from b_app import app


class Config:
    #  configuration settings, database URI and spotify API credentials
    SECRET_KEY = ('secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('db_uri')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SPOTIPY_CLIENT_ID = os.environ.get('client_id')

app.config.from_object(Config) #  load configuration from COnfig class
