import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'CLAVE_SECRETA'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:081122@localhost/IDGS805BD'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
