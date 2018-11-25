import json

with open('parks-and-greens-spaces.json') as json_file:
    data = json.load(json_file)

def getPark(name):

    for record in data:
        parkData = record['fields']
        site_name = parkData['site_name']

        if (site_name == name):
            print(parkData)
            return parkData

    print("Park not found")
    return 0

def getAllParkNames():
    parkNames = []

    for record in data:
        parkData = record['fields']
        site_name = parkData['site_name']
        id = parkData['objectid']
        parkNames.append({'id': id, 'siteName': site_name})

    return parkNames

def getNearestParks(lat, long):
    lat = 51.437975
    long = -2.590024

    parkNames = []

    i = 0

    for record in data:
        parkData = record['fields']
        if i == 0:
            print(parkData['geo_point_2d'])
        i += 1
        point = parkData['geo_point_2d'][0]

    return 0

#getNearestParks(0, 0)

