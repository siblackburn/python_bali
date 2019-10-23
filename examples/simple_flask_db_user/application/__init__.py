from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin, UserManager

from .config import ProductionConfig

db = SQLAlchemy()


# define the user model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    email_confirmed_at = db.Column(db.DateTime())

    # User information
    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(ProductionConfig)
    db.init_app(app)

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)

    with app.app_context():

        # Imports
        from . import routes

        # Create tables for our models
        db.create_all()

        return app