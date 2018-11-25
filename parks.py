import requests

url = 'https://opendata.bristol.gov.uk/api/records/1.0/search/'

params = dict(
  dataset='parks-and-greens-spaces',
)

response = requests.get(url=url, params=params)

if response.status_code != 200:
    print("API Request failed")
else:
    data = response.json()

parks = {}

for record in data['records']:

    field = record['fields']
    objectid = field['objectid']
    site_name = field['site_name']
    geo_shape = field['geo_shape']

    park = {objectid: [site_name, geo_shape]}

    parks.update(park)

#print(parks.keys())

