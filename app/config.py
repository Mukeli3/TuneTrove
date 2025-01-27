#!/usr/bin/python3

import os

class Config:
    """
    base config, contains default settings
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') # session and JWT secret key

    # db config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

    # silence tracking modifications warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT config
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    JWT_HEADER_TYPE = 'Bearer'

    DEBUG = False
    TESTING = False
