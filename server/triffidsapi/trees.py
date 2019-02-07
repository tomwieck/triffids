import json
import requests
import os

# Read trees.json
baseDirectory = os.path.join(os.path.dirname(__file__), '..')

with open(baseDirectory + '/data/trees.json') as json_file:
    data = json.load(json_file)

url = "https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees"


def getTreeById(id):
    query = "&q=recordid%3D" + str(id) + \
            "&facet=feature_type_name&facet=common_name&refine.feature_type_name=Tree+-+Parks+and+Green+Space"

    response = requests.get(url + query)
    response = response.json()
    data = response['records']

    if data:
        return data[0]


def getTreesByPark(parkCode):
    query = "&q=site_code%3D" + str(parkCode) + "&rows=1000" + "&facet=feature_type_name&facet=common_name"

    response = requests.get(url + query)
    response = response.json()
    data = response['records']

    if data:
        return data


def getTotalNumbTreesByPark(parkCode):
    trees = getTreesByPark(parkCode)

    return len(trees)


def getTreesBySpecies(parkCode, latinCode):
    query = "&q=site_code%3D" + str(parkCode) + "%2C+latin_code%3D" + str(latinCode) + \
            "&rows=1000&facet=feature_type_name&facet=common_name"

    response = requests.get(url + query)
    response = response.json()
    data = response['records']

    if data:
        return data


def getNumbUniqueSpeciesByPark(parkCode):
    # Get all trees within park
    trees = getTreesByPark(parkCode)

    species = []

    # Extract species of every tree in park
    for tree in trees:
        species.append(tree['latin_code'])

    # Convert list to set to get all unique instances of species
    species = set(species)

    return len(species)


def getTreesByLocation(lat, lng, radius):
    trees = []

    query = "&geofilter.distance=" + str(lat) + "%2C+" + str(lng) + "%2C+" + str(radius) + "&rows=20"

    response = requests.get(url + query)
    response = response.json()
    data = response['records']

    for record in data:
        treeData = record['fields']
        trees.append(treeData)

    return trees


def getUniqueSpecies(parkCode):
    # Get all trees within park
    trees = getTreesByPark(parkCode)

    species = []

    # Extract species of every tree in park
    for tree in trees:
        species.append(tree['fields']['latin_code'])

    # Convert list to set to get all unique instances of species
    species = set(species)
    return species


# print(getTreesByPark("VICTPA"))

# getTreesBySpecies('VICTPA', 'QURO')

# getTreesByLocation(51.44, -2.587, 500)

# print(getUniqueSpecies('VICTPA'))

# print(getTotalNumbTreesByPark('VICTPA'))