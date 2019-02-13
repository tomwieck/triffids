import json
import requests
import os
from . import trees

# Read parks json
baseDirectory = os.path.join(os.path.dirname(__file__), '..')

with open(baseDirectory + '/data/parks-and-greens-spaces.json') as json_file:
    data = json.load(json_file)


def getPark(code):
    # Example 'code' CUMBBASO
    park = []
    for record in data:
        parkData = record['fields']
        site_code = parkData['site_code']

        if (site_code == code):
            total_trees = trees.getTotalNumbTreesByPark(parkData['site_code'])
            unique_trees = trees.getNumbUniqueSpeciesByPark(
                parkData['site_code'])
            park.append({
                'id': str(parkData['site_code']),
                'siteName': str(parkData['site_name']),
                'unique_trees': str(unique_trees),
                'total_trees': str(total_trees),
                'lat': parkData['geo_point_2d'][0],
                'lng': parkData['geo_point_2d'][1],
                'geoShape': parkData['geo_shape']
            })
            print(park)
            return park

    print('Park not found')
    return 0


def getAllParkNames(page, lat=0, long=0):
    parksPerPage = 20
    lowestBoundary = (parksPerPage * page) - parksPerPage
    highestBoundary = parksPerPage * page - 1
    parkNames = []

    for index, record in enumerate(sorted(data, key=lambda x: x['fields']['site_name'])):
        if (index < lowestBoundary or index > highestBoundary):
            continue
        parkData = record['fields']
        total_trees = trees.getTotalNumbTreesByPark(parkData['site_code'])
        unique_trees = trees.getNumbUniqueSpeciesByPark(parkData['site_code'])

        parkNames.append({
            'id': str(parkData['site_code']),
            'siteName': str(parkData['site_name']),
            'unique_trees': str(unique_trees),
            'total_trees': str(total_trees)
        })

    return parkNames


def getNearestParks(lat, lng, radius):
    url = 'https://opendata.bristol.gov.uk/api/records/1.0/search/'
    dataset = '?dataset=parks-and-greens-spaces'
    sort = '&-sort=dist'
    geofilter = '&geofilter.distance=' + \
        str(lat) + '%2C+' + str(lng) + '%2C+' + str(radius)
    response = requests.get(url + dataset + sort + geofilter)
    response = response.json()

    records = response['records']
    parks = []

    # Create output with required data
    for record in records:
        parkCode = str(record['fields']['site_code'])

        # Get number of trees in park
        #totalTrees = len(trees.getTreesByPark(parkCode))

        # Get number of unique species in park
        #uniqueSpecies = len(trees.getUniqueSpecies(parkCode))
        parkData = record['fields']
        total_trees = trees.getTotalNumbTreesByPark(parkData['site_code'])
        unique_trees = trees.getNumbUniqueSpeciesByPark(parkData['site_code'])

        parks.append({
            'id': str(parkData['site_code']),
            'siteName': str(parkData['site_name']),
            'lat': parkData['geo_point_2d'][0],
            'lng': parkData['geo_point_2d'][1],
            'dist': parkData['dist'],
            'total_trees': total_trees,
            'unique_trees': unique_trees
        })

    print(parks)
    return parks

    # Data required
    # site_name, site_code, lat, long, dist, noOfTrees, uniqueSpecies

# getPark('CUMBBASO')

# getNearestParks(51.439413, -2.589423, 150)
