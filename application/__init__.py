from flask import Flask
from application.views.frontend import frontend_blueprint
from application.views.login import login_blueprint

from application.extensions.database import db
from application.extensions.login import login_manager


def create_app(cfg):
    app = Flask(__name__)
    app.config.from_pyfile(cfg)
    configure_blueprints(app)
    configure_extensions(app)
    return app


def configure_blueprints(app):
    app.register_blueprint(frontend_blueprint)
    app.register_blueprint(login_blueprint)


def configure_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
