# -*- coding: utf-8 -*-
from nodeclassifier import app
from flask import request, jsonify
from flask.ext.restful import Api, Resource, reqparse
import os


api = Api(app)

class Root(Resource):
    def get(self):
        """ Returna list of endpoints """
        return jsonify({
            '/v1.0/': 'API root endpoint',
            })

api.add_resource(Root, '/v1.0/')

@app.route('/')
def index():
    return "Node Classifier"
