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
            '/v1.0/roles': 'API root endpoint',
            '/v1.0/rules': 'API root endpoint',
            '/v1.0/nodes': 'API root endpoint',
            })

class Roles(Resource):
    def  get(self):
        """ Return the role assigned to a node """
        return jsonify({
            'role': 'default'
            })

class Rules(Resource):
    def get(self):
        """ Return a list of rules"""
        return jsonify({
            'rule': 'rule 1',
            'rule': 'rule 2'
            })

class Nodes(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('manuafactuer', type=str, required=False,
                                   help='System Manufacter',
                                   location='json')
        self.reqparse.add_argument('productname', type=str, required=False,
                                   help='Model Name',
                                   location='json')
    def get(self):
        """ Return a list of know nodes """
        return jsonify({
            'node1': 'nodedata',
            'node2': 'nodedata',
            })
    def put(self):
        """ Add a node and its data to the system """

        node
        return jsonify({
            'node': 'node_uuid',
            })


api.add_resource(Root, '/v1.0/')
api.add_resource(Roles, '/v1.0/roles')
api.add_resource(Rules, '/v1.0/rules')
api.add_resource(Nodes, '/v1.0/nodes')


@app.route('/')
def index():
    return "Node Classifier"
