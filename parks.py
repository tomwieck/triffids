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
        parkNames.append(site_name)

    return parkNames

getAllParkNames()