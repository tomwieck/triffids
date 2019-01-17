import json
import geopy.distance

with open('parks-and-greens-spaces.json') as json_file:
    data = json.load(json_file)


def getPark(code):
    # Example 'code' CUMBBASO
    park = []
    for record in data:
        parkData = record['fields']
        site_code = parkData['site_code']

        if (site_code == code):
            park.append({
                'id': str(parkData['site_code']),
                'siteName': str(parkData['site_name']),
                'lat': parkData['geo_point_2d'][0],
                'long': parkData['geo_point_2d'][1],
                'geoShape': parkData['geo_shape']
            })
            print(park)
            return park

    print("Park not found")
    return 0


def getAllParkNames():
    parkNames = []

    for record in data:
        parkData = record['fields']
        parkNames.append({
            'id': str(parkData['site_code']),
            'siteName': str(parkData['site_name'])
        })

    return parkNames

# TODO - Get location lat and long and locate nearest parks

def getNearestParks(lat, long):
    lat = 51.439413
    long = -2.589423

    # 51.4545, 2.5879, center of Bristol, default values?
    # If no lat long, either use this or getAllParkNames()

    parkNames = []

    i = 0

    for record in data:
        parkData = record['fields']
        if i == 0:
            print(parkData['geo_point_2d'])
        i += 1
        point = parkData['geo_point_2d'][0]

    return 0


# getPark("CUMBBASO")