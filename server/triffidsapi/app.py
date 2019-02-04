"""
app.py
- create a Flask app instance
"""

from flask import Flask
from flask_cors import CORS


def create_app(app_name='TRIFFIDS_API'):
    app = Flask(app_name)
    # app.config.from_object('surveyapi.config.BaseConfig')
    CORS(app)
    from triffidsapi.api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return app
