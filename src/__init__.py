import os

# import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# instantiate the db
db = SQLAlchemy()

# print(app.config, file=sys.stderr)

# adding Application Factory pattern
def create_app(script_info=None):

    # instantiate app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from src.api.normalize import normalize_blueprint
    app.register_blueprint(normalize_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
