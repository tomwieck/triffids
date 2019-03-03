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

    totalTrees, uniqueTrees = trees.getTreeNumbers(parkData['site_code'])

    if totalTrees == 0:
        return []

    park = {
        'id': str(parkData['site_code']),
        'siteName': str(parkData['site_name']),
        'unique_trees': str(uniqueTrees),
        'total_trees': str(totalTrees),
        'lat': parkData['geo_point_2d'][0],
        'lng': parkData['geo_point_2d'][1],
        'geoShape': parkData['geo_shape']
    }

    return park


def getAllParkNames(page, lat=0, long=0):
    parksPerPage = 8
    lowestBoundary = (parksPerPage * page) - parksPerPage
    highestBoundary = parksPerPage * page - 1
    parkNames = []

    for index, record in enumerate(sorted(data, key=lambda x: x['fields']['site_name'])):
        if (index < lowestBoundary or index > highestBoundary):
            continue
        parkData = record['fields']

        totalTrees, uniqueTrees = trees.getTreeNumbers(parkData['site_code'])

        if totalTrees == 0:
            continue

        parkNames.append({
            'id': str(parkData['site_code']),
            'siteName': str(parkData['site_name']),
            'unique_trees': str(uniqueTrees),
            'total_trees': str(totalTrees)
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
        # Get number of unique species in park
        parkData = record['fields']
        parkCode = str(record['fields']['site_code'])

        totalTrees, uniqueTrees = trees.getTreeNumbers(parkCode)

        if totalTrees == 0:
            continue

        parks.append({
            'id': str(parkData['site_code']),
            'siteName': str(parkData['site_name']),
            'lat': parkData['geo_point_2d'][0],
            'lng': parkData['geo_point_2d'][1],
            'dist': parkData['dist'],
            'total_trees': totalTrees,
            'unique_trees': uniqueTrees
        })

    if parks:
        return parks
    else:
        return []

    # Data required
    # site_name, site_code, lat, long, dist, noOfTrees, uniqueSpecies


def getParkInfo(parkCode):
    targetFilePath = baseDirectory + \
        '/data/parkinfo/' + str(parkCode) + '.html'
    defaultFilePath = baseDirectory + '/data/parkinfo/' + 'DEFAULT.html'
    if os.path.isfile(targetFilePath):
        fh = open(targetFilePath, 'r')
    else:
        fh = open(defaultFilePath, 'r')

    data = fh.read()
    return data


# print(getPark('VICTPA'))

# print(getNearestParks(51.44,-2.587,600))

# (getAllParkNames(1))

# getParkInfo('VICTKPA')
