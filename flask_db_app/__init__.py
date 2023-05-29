import os

from flask import Flask

from flask_db_app.db import get_db


def create_app():
    """Creates and configures the Flask application.

    Returns:
        app(Flask): The configured Flask application instance.

    Configuration options are set with 'app.config.from_mapping'
    Database is initialized by 'db.init_app(app)'
    Blueprint for the music.py is registered by 'app.register_blueprint(music.bp)'
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask_db_app.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import music
    app.register_blueprint(music.bp)

    return app
