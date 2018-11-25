import json

def getTrees(siteCode, lat, long):

    with open('trees.json') as json_file:
        data = json.load(json_file)

    trees = {}

    if (lat == 0 and long == 0):

        for record in data:

            treeData = record['fields']

            if (siteCode == treeData['site_code']):
                trees.update(treeData)

        if (bool(trees) == False):
            print("No trees found in that area")
        else:
            return trees

    else:
        for record in data:

            treeData = record['fields']
            treeLat = treeData['geo_point_2d'][0]
            treeLong = treeData['geo_point_2d'][1]

            if (treeLat == lat and treeLong == long):
                return treeData

        print("No trees found at that coordinate point")
        return 0

