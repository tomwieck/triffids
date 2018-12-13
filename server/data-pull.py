import requests
url = 'https://opendata.bristol.gov.uk/api/records/1.0/search/'

params = dict(
  dataset='trees',
  rows='10000'
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below
print('returned')

print(data)

tree_types = {}

for record in data['records']:
    if 'common_name' in record['fields']:
      tree_type = record['fields']['common_name']

      if tree_type in tree_types:
        amount = tree_types[tree_type]
      else:
        amount = 0

      tree_types[tree_type] = amount + 1

for key in tree_types:
  print (key, tree_types[key])

#print 'total:', len(tree_types)
