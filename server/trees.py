import json
# import xmltodict
# import pprint
# from xml.dom import minidom
# from decimal import Decimal


def getTrees(siteCode, lat, long):
    # Read trees.json
    with open('trees.json') as json_file:
        data = json.load(json_file)

    # with open('specialTrees.xml') as xml_file:
    #     specialTreeData = xmltodict.parse(xml_file.read())

    #print(specialTreeData)

    # for record in specialTreeData:
    #     pop = 0

    # Read specialTrees.json
    specialTrees = {}
    #xmldoc = minidom.parse('specialTrees.xml')
    #specialTreeList = xmldoc.getElementsByTagName('tree')
    # print(len(itemlist))
    # print(itemlist[0].attributes['name'].value)
    #print(specialTreeList)
    # for tree in specialTreeList:
    #     kvPair = {tree.attribut}
    #     print(s.attributes['name'].value)

    trees = []

    # Search for trees by park
    if (lat == 0 and long == 0):

        for record in data:

            treeData = record['fields']

            # Rounding to 6 decimal places to work with Richard Blands Special Tree collection dataset
            treeLat = treeData['geo_point_2d'][0]
            treeLong = treeData['geo_point_2d'][1]

            treeData['geo_point_2d'][0] = round(treeLat, 6)
            treeData['geo_point_2d'][1] = round(treeLong, 6)

            if (siteCode == treeData['site_code']):
                trees.append(treeData)

        if (bool(trees) == False):
            print("No trees found in that area")
            return trees
        else:
            #print(trees)
            return trees

    # Search for trees by coordinates
    else:
        for record in data:

            treeData = record['fields']
            treeLat = treeData['geo_point_2d'][0]
            treeLong = treeData['geo_point_2d'][1]

            if (treeLat == lat and treeLong == long):
                return treeData

        print("No trees found at that coordinate point")
        return trees



#getTrees("VICTPA", 0, 0)
