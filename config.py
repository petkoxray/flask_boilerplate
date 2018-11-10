import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join('.env'))


class Config:
    # App configurations
    SECRET_KEY = os.environ.get('SECRET_KEY') or "very-secret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Mail Server configurations
    MAIL_SERVER = os.environ.get('EMAIL_SERVER')
    MAIL_PORT = os.environ.get('EMAIL_PORT')
    MAIL_USE_TLS = os.environ.get('EMAIL_TLS')
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # Debug Toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
