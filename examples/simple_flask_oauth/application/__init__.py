from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from oauthlib.oauth2 import WebApplicationClient


from .config import DevelopmentConfig

db = SQLAlchemy()
oath_client = None

def create_app():
    global oath_client
    
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    # OAuth 2 client setup
    oath_client = WebApplicationClient(app.config['GOOGLE_CLIENT_ID'])

    with app.app_context():

        # Imports
        from . import routes

        # Create tables for our models
        db.create_all()

        return app