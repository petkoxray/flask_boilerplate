from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension
from config import Config

db = SQLAlchemy()
migrate = Migrate()
toolbar = DebugToolbarExtension()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from boilerplate.users.routes import users
    from boilerplate.pages.routes import pages
    from boilerplate.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(pages)
    app.register_blueprint(errors)

    return app
