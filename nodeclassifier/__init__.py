from flask import Flask, jsonify, request
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

import nodeclassifier.views, nodeclassifier.models

def register_blueprints(app):
    from nodeclassifier.views import rules
    app.register_blueprint(rules)

register_blueprints(app)
