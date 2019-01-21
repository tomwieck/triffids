import json
import requests
import os

# Read trees.json
baseDirectory = os.path.join(os.path.dirname(__file__), '..')

with open(baseDirectory + '/data/trees.json') as json_file:
    data = json.load(json_file)


def getTreesByPark(parkCode):
    trees = []

    # Search for trees by park
    for record in data:

        treeData = record['fields']

        if parkCode == treeData['site_code']:
            trees.append(treeData)

    if not bool(trees):
        # print("No trees found in that area")
        return trees
    else:
        return trees


def getTreesBySpecies(parkCode, latinCode):
    trees = []

    # Search for trees by park
    for record in data:

        treeData = record['fields']

        if parkCode == treeData['site_code'] and latinCode == treeData['latin_code']:
            trees.append(treeData)

    return trees


def getTreesByLocation(lat, lng, radius):
    url = "https://opendata.bristol.gov.uk/api/records/1.0/search/"
    dataset = "?dataset=trees"
    geofilter = "&geofilter.distance=" + str(lat) + "%2C+" + str(lng) + "%2C+" + str(radius)

    response = requests.get(url + dataset + geofilter)
    response = response.json()

    return response


def getUniqueSpecies(parkCode):

    # Get all trees within park
    trees = getTreesByPark(parkCode)

    species = []

    # Extract species of every tree in park
    for tree in trees:
        species.append(tree['latin_code'])

    # Convert list to set to get all unique instances of species
    species = set(species)
    return species


# getTrees("VICTPA", 0, 0)

# getTreesByLocation(51.440738652303786, -2.586997949748452, 50)

# getUniqueSpecies('VICTPA')
