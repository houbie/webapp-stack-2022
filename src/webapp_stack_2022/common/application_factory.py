import json
import os
from pathlib import Path

import flask
import serverless_wsgi
from connexion.apps.flask_app import FlaskApp
from flask import jsonify


def create_app(
    name,
    specification,
    specification_dir="../",
    base_path=None,
    options=None,
    resolver=None,
):
    """Create a connexion app with swagger_ui disabled by default"""

    if options is None:
        options = {"swagger_ui": False}
    connexion_app = FlaskApp(name, specification_dir=specification_dir, options=options)
    connexion_app.app.url_map.strict_slashes = False
    connexion_app.add_api(specification, base_path=base_path, resolver=resolver)
    serverless_wsgi.TEXT_MIME_TYPES.append("application/problem+json")  # mimetype of connexion validation errors

    connexion_app.app.logger.addHandler(flask.logging.default_handler)
    return connexion_app


def get_info():
    app_info = Path(os.environ.get("LAMBDA_TASK_ROOT", Path(__file__).parents[3]), "generated/app-info.json")
    with app_info.open() as file:
        app_info = json.load(file)
        app_info["region"] = os.environ.get("AWS_REGION", "?")
    return app_info


def info():
    try:
        return jsonify(get_info())
    except FileNotFoundError:
        return "No app-info.json found. Make sure to generate it during the build?", 500
