import json
import requests
# import os

# Read trees.json
# baseDirectory = os.path.join(os.path.dirname(__file__), '..')

# with open(baseDirectory + '/data/trees.json') as json_file:
#     data = json.load(json_file)

url = "https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees"


def getTreeById(id):
    query = "&q=recordid%3D" + str(id) + \
        "&refine.feature_type_name=Tree+-+Parks+and+Green+Space"

    response = requests.get(url + query)
    response = response.json()
    data = response['records']

    if data:
        return data[0]
    else:
        return []


def countTreesByPark(parkCode):
    query = "&q=site_code%3D" + str(parkCode) + "&rows=0"

    response = requests.get(url + query)
    response = response.json()
    data = response['nhits']
    if data:
        return data
    else:
        return 0


def getTreesByPark(parkCode):
    numTrees = str(countTreesByPark(parkCode))
    fields = "site_code,geo_point_2d,latin_code,latin_name,common_name,full_common_name,dbh,crown_area,crown_height"
    query = "&q=site_code%3D" + \
        str(parkCode) + "&rows=" + numTrees + \
        "&fields=" + fields

    response = requests.get(url + query)
    response = response.json()
    data = response['records']

    if data:
        return data
    else:
        return []


def getTreeNumbers(parkCode):
    trees = getTreesByPark(parkCode)

    totalTrees = len(trees)
    uniqueSpecies = len(getUniqueSpecies(trees))

    return totalTrees, uniqueSpecies


def getTreesBySpecies(parkCode, latinCode):
    fields = "site_code,latin_code,common_name,full_common_name,dbh,crown_area"
    query = "&q=site_code%3D" + str(parkCode) + "%2C+latin_code%3D" + \
            str(latinCode) + "&fields=" + fields + \
            "&rows=1000"

    response = requests.get(url + query)
    response = response.json()
    data = response['records']

    if data:
        return data
    else:
        return []


def getTreesByLocation(lat, lng, radius):
    trees = []

    query = "&geofilter.distance=" + \
        str(lat) + "%2C+" + str(lng) + "%2C+" + str(radius) + "&rows=1000"

    response = requests.get(url + query)
    response = response.json()
    data = response['records']

    for record in data:
        treeData = record['fields']
        trees.append(treeData)

    if trees:
        return trees
    else:
        return []


def getUniqueSpecies(trees):
    # Get all trees within park
    # trees = getTreesByPark(parkCode)

    species = set()

    # Extract species of every tree in park
    if trees:
        for tree in trees:
            if 'latin_code' in tree['fields']:
                species.add(tree['fields']['latin_code'])

    return species

# print(getTreesByPark("VICTPA"))

# getTreesBySpecies('VICTPA', 'QURO')

# getTreesByLocation(51.44, -2.587, 500)

# print(getUniqueSpecies('VICTPA'))

# print(getTotalNumbTreesByPark('VICTPA'))
