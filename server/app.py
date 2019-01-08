#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
from flask_cors import CORS

import benches
import parks
import trees

app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/server/park/<string:code>', methods=['GET'])
def getPark(code):
    response = parks.getPark(code)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/server/allParkNames', methods=['GET'])
def getAllParkNames():
    response = parks.getAllParkNames()
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/server/nearestParks/<string:lat>/<string:long>', methods=['GET'])
def getNearestParks(lat, long):
    response = parks.getNearestParks(lat, long)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@app.route('/server/trees/<string:siteCode>/<string:lat>/<string:long>', methods=['GET'])
def getTrees(siteCode, lat, long):
    response = trees.getTrees(siteCode, lat, long)
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
