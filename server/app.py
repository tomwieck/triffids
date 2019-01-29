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
    page = request.args.get('page')
    lat = request.args.get('lat')
    long = request.args.get('long')

    response = parks.getAllParkNames(int(page), lat, long)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/parks/<string:parkCode>', methods=['GET'])
def getPark(parkCode):
    response = parks.getPark(parkCode)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/parks/lat=<string:lat>&lng=<string:lng>&radius=<string:radius>', methods=['GET'])
def getNearestParks(lat, lng, radius):
    response = parks.getNearestParks(lat, lng, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/trees/<string:parkCode>', methods=['GET'])
def getTrees(parkCode):
    latinCode = request.args.get('latinCode')

    # If no latin code provided, show all trees in park. Else, filter by species
    if latinCode is None:
        response = trees.getTreesByPark(parkCode)
    else:
        response = trees.getTreesBySpecies(parkCode, latinCode)

    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/trees/lat=<string:lat>&lng=<string:lng>&radius=<string:radius>', methods=['GET'])
def getTreesByLocation(lat, lng, radius):
    response = trees.getTreesByLocation(lat, lng, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/api/v1/benches/lat=<string:lat>&lng=<string:lng>&radius=<string:radius>', methods=['GET'])
def getBenches(lat, lng, radius):
    response = benches.getBenches(lat, lng, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
