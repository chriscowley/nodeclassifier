from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.from_object('config')

import nodeclassifier.views

