import json
import requests
import os

# Read trees.json
baseDirectory = os.path.join(os.path.dirname(__file__), '..')

with open(baseDirectory + '/data/trees.json') as json_file:
    data = json.load(json_file)


def getTreeById(id):

    url = "https://opendata.bristol.gov.uk/api/records/1.0/search/"
    dataset = "?dataset=trees"
    geofilter = "&q=recordid%3D" + str(id) + "&facet=feature_type_name&facet=common_name"

    response = requests.get(url + dataset + geofilter)
    response = response.json()
    data = response['records']

    if data:
        return data[0]


def getTreesByPark(parkCode):
    trees = []

    # Search for trees by park
    for record in data:

        id = record['recordid']
        treeData = record['fields']

        if parkCode == treeData['site_code']:
            treeData['id'] = id
            trees.append(treeData)

    return trees

def getTotalNumbTreesByPark(parkCode):
    trees = 0
    for record in data:
        treeData = record['fields']
        if parkCode == treeData['site_code']:
            trees = trees + 1

    return trees

def getTreesBySpecies(parkCode, latinCode):
    trees = []

    # Search for trees by park
    for record in data:

        treeData = record['fields']

        if parkCode == treeData['site_code'] and latinCode == treeData['latin_code']:
            trees.append(treeData)

    print(trees)
    print(len(trees))
    return trees

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

    url = "https://opendata.bristol.gov.uk/api/records/1.0/search/"
    dataset = "?dataset=trees"
    geofilter = "&geofilter.distance=" + str(lat) + "%2C+" + str(lng) + "%2C+" + str(radius)

    response = requests.get(url + dataset + geofilter)
    response = response.json()
    data = response['records']

    for record in data:
        treeData = record['fields']
        trees.append(treeData)

    print(trees)
    print(len(trees))
    return trees


def getUniqueSpecies(parkCode):

    # Get all trees within park
    trees = getTreesByPark(parkCode)

    species = []

    # Extract species of every tree in park
    for tree in trees:
        species.append(tree['latin_code'])

    # Convert list to set to get all unique instances of species
    species = set(species)
    print(species)
    return species


# getTreesByPark("VICTPA")

# getTreesBySpecies('VICTPA', 'QURO')

# getTreesByLocation(51.44, -2.587, 500)

# getUniqueSpecies('VICTPA')
