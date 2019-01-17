import json
import requests

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

def getNearestParks(lat, lng, radius):

    url = 'https://opendata.bristol.gov.uk/api/records/1.0/search/'

    params = dict(
        lat=lat,
        lng=lng,
        radius=radius
    )

    resp = requests.get(url=url, params=params)
    data = resp.json()


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
