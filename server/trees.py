import json
import requests

# Read trees.json
with open('trees.json') as json_file:
    data = json.load(json_file)


def getTreesByPark(parkCode):
    trees = []

    # Search for trees by park
    for record in data:

        treeData = record['fields']

        if parkCode == treeData['site_code']:
            trees.append(treeData)

    if not bool(trees):
        print("No trees found in that area")
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


# TODO - Search by radius, currently returning singular tree
def getTreesByLocation(lat, lng, radius):
    url = 'https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&geofilter.distance=' \
          + str(lat) + "%2C+" + str(lng) + "%2C+" + str(radius)

    response = requests.get(url)

    response = response.json()

    print(response)

    return response


# getTrees("VICTPA", 0, 0)

getTreesByLocation(51.440738652303786, -2.586997949748452, 50)
