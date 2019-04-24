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
    if not response:
        abort(404)
    return jsonify(response)


@api.route('/parks/<string:parkCode>', methods=['GET'])
def getPark(parkCode):
    response = parks.getPark(parkCode)
    if not response:
        abort(404)
    return jsonify(response)


@api.route('/parks/loc', methods=['GET'])
def getNearestParks():
    lat = request.args.get('lat') or 0
    lng = request.args.get('lng') or 0
    radius = request.args.get('radius')

    response = parks.getNearestParks(lat, lng, radius)
    print(response)
    if not response:
        abort(404)
    return jsonify(response)


@api.route('/parks/info/<string:parkCode>', methods=['GET'])
def getParkInfo(parkCode):
    response = parks.getParkInfo(parkCode)
    if not response:
        abort(404)
    return response


@api.route('/trees', methods=['GET'])
def getTree():
    treeId = request.args.get('id')

    response = trees.getTreeById(treeId)
    if not response:
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

    if not response:
        abort(404)
    return jsonify(response)


@api.route('/trees/loc', methods=['GET'])
def getTreesByLocation():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    radius = request.args.get('radius')

    response = trees.getTreesByLocation(lat, lng, radius)
    if not response:
        abort(404)
    return jsonify(response)


@api.route('/benches/loc', methods=['GET'])
def getBenches():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    radius = request.args.get('radius')

    response = benches.getBenches(lat, lng, radius)

    if not response:
        abort(404)
    return jsonify(response)
