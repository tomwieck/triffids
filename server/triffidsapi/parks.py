import json
import requests
import os

if __name__ == '__main__':
    import trees
else:
    from . import trees


# Read parks json
baseDirectory = os.path.join(os.path.dirname(__file__), '..')

with open(baseDirectory + '/data/parks-and-greens-spaces.json') as json_file:
    data = json.load(json_file)


def getPark(code):
    # Example 'code' CUMBBASO
    url = 'https://opendata.bristol.gov.uk/api/records/1.0/search/'
    dataset = '?dataset=parks-and-greens-spaces'
    query = '&q=site_code%3A+' + str(code)

    response = requests.get(url + dataset + query)
    response = response.json()

    if response:
        parkData = response['records'][0]['fields']
    else:
        return []

    total_trees = trees.getTotalNumbTreesByPark(parkData['site_code'])

    if total_trees == 0:
        return []

    unique_trees = trees.getNumbUniqueSpeciesByPark(parkData['site_code'])

    park = {
        'id': str(parkData['site_code']),
        'siteName': str(parkData['site_name']),
        'unique_trees': str(unique_trees),
        'total_trees': str(total_trees),
        'lat': parkData['geo_point_2d'][0],
        'lng': parkData['geo_point_2d'][1],
        'geoShape': parkData['geo_shape']
    }

    return park


def getAllParkNames(page):
    parksPerPage = 20
    lowestBoundary = (parksPerPage * page) - parksPerPage  # 20
    highestBoundary = parksPerPage * page - 1  # 39
    parkNames = []

    for index, record in enumerate(data):
        if (index < lowestBoundary or index > highestBoundary):
            continue
        parkData = record['fields']
        total_trees = trees.getTotalNumbTreesByPark(parkData['site_code'])

        if total_trees == 0:
            continue

        unique_trees = trees.getNumbUniqueSpeciesByPark(parkData['site_code'])

        parkNames.append({
            'id': str(parkData['site_code']),
            'siteName': str(parkData['site_name']),
            'unique_trees': str(unique_trees),
            'total_trees': str(total_trees)
        })

    if parkNames:
        return parkNames
    else:
        return []


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
        totalTrees = trees.getTotalNumbTreesByPark(parkCode)

        if totalTrees == 0:
            continue
            
        # Get number of unique species in park
        uniqueSpecies = trees.getNumbUniqueSpeciesByPark(parkCode)

        parks.append({
            'id': parkCode,
            'siteName': str(record['fields']['site_name']),
            'lat': record['fields']['geo_point_2d'][0],
            'lng': record['fields']['geo_point_2d'][1],
            'dist': record['fields']['dist'],
            'totalTrees': totalTrees,
            'uniqueSpecies': uniqueSpecies
        })

    if parks:
        return parks
    else:
        return []

    # Data required
    # site_name, site_code, lat, long, dist, noOfTrees, uniqueSpecies

# getPark('CUMBBASO')

# print(getNearestParks(51.439413, -2.589423, 150))

# (getAllParkNames(1))