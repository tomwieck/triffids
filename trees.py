import requests

url = 'https://opendata.bristol.gov.uk/api/records/1.0/search/'

params = dict(
  dataset='trees',
)

response = requests.get(url=url, params=params)


if response.status_code != 200:
    print("API Request failed")
else:
    data = response.json()


trees = {}

for record in data['records']:

    field = record['fields']

    if field['type'] == 'Tree - Parks and Green Space':
        asset_id = field['asset_id']
        site_name = field['site_name']
        full_common_name = field['full_common_name']
        latin_name = field['latin_name']
        geo_shape = field['geo_shape']
        dbh = field['dbh']
        type = field['type']

        tree = {asset_id: [full_common_name, latin_name, site_name, dbh, geo_shape, type]}

        trees.update(tree)

print(trees.values())
