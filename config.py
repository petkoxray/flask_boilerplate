import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # App configurations
    SECRET_KEY = os.environ.get('SECRET_KEY') or "very-secret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir, 'site.db')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
