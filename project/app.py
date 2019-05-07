from flask import Flask

from .home.views import blueprint as home_blueprint
from .main.views import blueprint as main_blueprint
from .extensions import db, flask_bcrypt


def create_app():
    """Create a Flask application using the app factory pattern.

    :param settings_override: Override settings (for testing)
    :return: Flask app
    """
    app = Flask(__name__)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    app.config['SWAGGER_UI_JSONEDITOR'] = True  # FJE change swagger from json object to fields

    app.register_blueprint(home_blueprint)
    app.register_blueprint(main_blueprint)
    register_extensions(app)

    return app


def register_extensions(app):
    """Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return None
