import json


def getTreesByPark(parkCode):
    # Read trees.json
    with open('trees.json') as json_file:
        data = json.load(json_file)

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
    # Read trees.json
    with open('trees.json') as json_file:
        data = json.load(json_file)

    trees = []

    # Search for trees by park
    for record in data:

        treeData = record['fields']

        if parkCode == treeData['site_code'] and latinCode == treeData['latin_code']:
            trees.append(treeData)

    return trees


# TODO - Search by radius, currently returning singular tree
def getTreesByLocation(lat, long):
    # Read trees.json
    with open('trees.json') as json_file:
        data = json.load(json_file)

    trees = []

    # Search for trees by coordinates
    for record in data:

        treeData = record['fields']
        treeLat = treeData['geo_point_2d'][0]
        treeLong = treeData['geo_point_2d'][1]

        if treeLat == lat and treeLong == long:
            return treeData

    print("No trees found at that coordinate point")
    return trees

# getTrees("VICTPA", 0, 0)
