#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS

import sys
sys.path.append('triffidsapi')

import parks
import trees
import benches

app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/v1/parks', methods=['GET'])
def getAllParkNames():
    response = parks.getAllParkNames()
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/parks/<string:parkCode>', methods=['GET'])
def getPark(parkCode):
    response = parks.getPark(parkCode)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/parks?lat=<string:lat>&lng=<string:lng>&radius=<string:radius>', methods=['GET'])
def getNearestParks(lat, lng, radius):
    response = parks.getNearestParks(lat, lng, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/trees/<string:parkCode>', methods=['GET'])
def getTreesByPark(parkCode):
    response = trees.getTreesByPark(parkCode)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/trees/<string:parkCode>?latincode=<string:latinCode>', methods=['GET'])
def getTreesBySpecies(parkCode, latinCode):
    response = trees.getTreesBySpecies(parkCode, latinCode)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/trees?lat=<string:lat>&lng=<string:lng>&radius=<string:radius>', methods=['GET'])
def getTreesByLocation(lat, lng, radius):
    response = trees.getTreesByLocation(lat, lng, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/server/benches/<string:lat>/<string:long>/<string:radius>', methods=['GET'])
def getBenches(lat, long, radius):
    response = benches.getBenches(lat, long, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
