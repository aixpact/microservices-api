from flask import Flask
from importlib import import_module
# from .home import blueprint
from .home.views import blueprint


# def register_blueprints(app):
#     for module_name in ('hello',):
#         module = import_module('hello_app.{}.views'.format(module_name))
#         app.register_blueprint(module.blueprint)


def create_app():
    """Create a Flask application using the app factory pattern.

    :param settings_override: Override settings (for testing)
    :return: Flask app
    """
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    # register_blueprints(app)

    return app
