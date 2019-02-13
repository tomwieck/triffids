"""
api.py
- api endpoints for the Triffids server
"""

from flask import Blueprint, make_response, abort, jsonify, request

from . import trees, parks, benches

api = Blueprint('api', __name__)


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@api.route('/')
def index():
    return "Hello, World!"


@api.route('/parks', methods=['GET'])
def getAllParkNames():
    lat = request.args.get('lat') or 0
    lng = request.args.get('lng') or 0
    rad = request.args.get('rad') or 1000
    page = request.args.get('page') or 1
    if lat == 0 or lng == 0:
        response = parks.getAllParkNames(int(page))
    else:
        response = parks.getNearestParks(lat, lng, rad)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@api.route('/parks/<string:parkCode>', methods=['GET'])
def getPark(parkCode):
    response = parks.getPark(parkCode)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@api.route('/parks/lat=<string:lat>&lng=<string:lng>&radius=<string:radius>', methods=['GET'])
def getNearestParks(lat, lng, radius):
    lat = request.args.get('lat') or 0
    lng = request.args.get('lng') or 0
    response = parks.getNearestParks(lat, lng, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@api.route('/tree/<string:treeId>', methods=['GET'])
def getTree(treeId):
    response = trees.getTreeById(treeId)

    if len(response) == 0:
        abort(404)
    return jsonify(response)


@api.route('/trees/<string:parkCode>', methods=['GET'])
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


@api.route('/trees/lat=<string:lat>&lng=<string:lng>&radius=<string:radius>', methods=['GET'])
def getTreesByLocation(lat, lng, radius):
    response = trees.getTreesByLocation(lat, lng, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)


@api.route('/benches/lat=<string:lat>&lng=<string:lng>&radius=<string:radius>', methods=['GET'])
def getBenches(lat, lng, radius):
    response = benches.getBenches(lat, lng, radius)
    if len(response) == 0:
        abort(404)
    return jsonify(response)
