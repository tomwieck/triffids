import json

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
                'id': parkData['site_code'],
                'siteName': parkData['site_name'],
                'geoPoint': parkData['geo_point_2d'],
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
            'id': parkData['site_code'],
            'siteName': parkData['site_name']
        })

    return parkNames

def getNearestParks(lat, long):
    lat = 51.437975
    long = -2.590024

    # 51.4545, 2.5879, center of Bristol, default values?
    # If no lat long, either use this or getAllParkNames()

    parkNames = []

    i = 0

    for record in data:
        parkData = record['fields']
        import pdb; pdb.set_trace()
        if i == 0:
            print(parkData['geo_point_2d'])
        i += 1
        point = parkData['geo_point_2d'][0]

    return 0
    # return
    # site_name -> siteName
    # objectid / site_code(?) -> id
    # geo_point_2d[0, 1] -> {lat: 0, long: 0}


#getNearestParks(0, 0)

