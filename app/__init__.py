from flask import Flask
from flask_bootstrap import Bootstrap
##from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
##db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

# Initializing flask extensions
    bootstrap.init_app(app)
    ##db.init_app(app)

# Creating the app configurations
    app.config.from_object(config_options[config_name])

# Registering the blueprint
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint,url_prefix = '/eventsbuddy/admin')
    
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint,url_prefix = '/')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/eventsbuddy/authenticate')

    return app