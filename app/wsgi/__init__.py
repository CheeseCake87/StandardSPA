from flask import Flask, url_for, redirect

from app.wsgi.config import flask_config, imp_config
from app.wsgi.extensions import imp, vt, db


def create_app(builder: str = "flask"):
    app = Flask(__name__, static_url_path="/")
    app.config.from_object(flask_config.as_object())
    imp.init_app(app, imp_config)

    db.init_app(app)

    if builder == "flask":
        vt.init_app(app, cors_allowed_hosts=["http://127.0.0.1:5002"])
        imp.import_app_resources()
        imp.import_blueprint("api")
        imp.import_blueprint("testing")

    imp.import_models("models")
    with app.app_context():
        db.create_all()

    return app
