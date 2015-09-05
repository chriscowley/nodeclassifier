# -*- coding: utf-8 -*-
from nodeclassifier import app
from flask import request, jsonify, Blueprint, redirect, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.views import MethodView
import os
from uuid import uuid4
import json
import io
from nodeclassifier.models import Rule, Condition

rules = Blueprint('rules', __name__)

api = Api(app)


class Root(Resource):
    def get(self):
        """ Return a list of endpoints """
        return jsonify({
            '/v1.0/': 'API root endpoint',
            '/v1.0/roles': 'API root endpoint',
            '/v1.0/rules': 'API root endpoint',
            '/v1.0/nodes': 'API root endpoint',
            })


class Roles(Resource):
    def get(self):
        """ Return the role assigned to a node """
        return jsonify({
            'role': 'default'
            })


class Rules(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('role', type=str, required=False,
                                   help='Role to the this rule which match',
                                   location='json')
        super(Rules, self).__init__()

    def get(self):
        """ Return a list of rules"""
        novarule = {'productname': 'Microserver'}
        storagerule = {'product': 'Atomboard'}
#        rules = Rules.objects.all()
        rules = {
                'novanode': novarule,
                'storage': storagerule
                }
        return rules

    def post(self):
        """ Add a new rule """
        uuid = str(uuid4()).replace('-', '')[:32]
        args = self.reqparse.parse_args()
        role = args['role']
        rule = {
                'uuid': uuid,
                'role': role,
               }
        return jsonify(rule)


class Nodes(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('manufacturer', type=str, required=False,
                                   help='System Manufacter',
                                   location='json')
        self.reqparse.add_argument('productname', type=str, required=False,
                                   help='Model Name',
                                   location='json')
        super(Nodes, self).__init__()

    def get(self):
        """ Return a list of know nodes """
        return jsonify({
            'node1': 'nodedata',
            'node2': 'nodedata',
            })

    def post(self):
        """ Add a node and its data to the system """
        uuid = str(uuid4()).replace('-', '')[:32]
        args = self.reqparse.parse_args()
        manufacturer = args['manufacturer']
        productname = args['productname']
        nodefile = os.path.join(app.config['DATADIR'], uuid + '.json')

        nodedata = {
                'uuid': uuid,
                'manufacturer': args['manufacturer'],
                'productname': args['productname']
                }
        with io.open(nodefile, 'w', encoding='utf-8') as outfile:
            outfile.write(unicode(json.dumps(nodedata, ensure_ascii=False)))
        return jsonify(nodedata)


class Node(Resource):
    def get(self, nodename):
        """ Detailed data about a node """
        return jsonify({
            'nodename': 'node1',
            'manufacturer': 'Dell',
            'productname': 'XPS-420',
            })


class Role(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('manufacturer', type=str, required=False,
                                   help='System Manufacter',
                                   location='json')
        self.reqparse.add_argument('productname', type=str, required=False,
                                   help='Model Name',
                                   location='json')
        super(Role, self).__init__()

    def get(self):
        """ Return a role based on parameters passes in the JSON """
        args = self.reqparse.parse_args()
        productname = args['productname']
        if productname == 'XPS420':
            role = 'desktop'
        else:
            role = 'default'
        return {'role': role}, 200


api.add_resource(Root, '/v1.0/')
api.add_resource(Roles, '/v1.0/roles')
api.add_resource(Role, '/v1.0/role')
api.add_resource(Rules, '/v1.0/rules')
api.add_resource(Nodes, '/v1.0/nodes')
api.add_resource(Node, '/v1.0/nodes/<string:nodename>')


@app.route('/')
def index():
    return "Node Classifier"
