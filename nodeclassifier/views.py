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

class GetRole(Resource):
    def  get(self):
        """ Return the role assigned to a node """
        return jsonify({
            'role': 'default'
            })

api.add_resource(Root, '/v1.0/')
api.add_resource(GetRole, '/v1.0/getrole')

@app.route('/')
def index():
    return "Node Classifier"
