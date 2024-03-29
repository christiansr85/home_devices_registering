import markdown
import os
import shelve

from flask import Flask, g
from flask_restful import Api, Resource, reqparse

# Flask instance
app = Flask(__name__)

# Flask api
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open('devices.db')
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

class DeviceList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])

        return { 'data': devices }

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('device_type', required=True)
        parser.add_argument('controller_gateway', required=True)

        # Build the object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return { 'data': args }, 201

class Device(Resource):
    def get(self, identifier):
        shelf = get_db()

        # 404 if the device doesn't exist in the data store
        if not (identifier in shelf):
            return { 'data': {} }, 404

        return { 'data': shelf[identifier] }, 200

    def delete(self, identifier):
        shelf = get_db()

        # 404 if the device doesn't exist in the data store
        if not (identifier in shelf):
            return { 'data': {} }, 404

        del shelf[identifier]
        return '', 204

api.add_resource(DeviceList, '/devices')
api.add_resource(Device, '/device/<string:identifier>')