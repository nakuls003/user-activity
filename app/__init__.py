from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    db.init_app(app)
    ma.init_app(app)

    return app
