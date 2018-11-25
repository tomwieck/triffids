import urllib, json
from urllib.request import Request, urlopen
import json
import urllib

params = dict(
    latitude='51.234',
    longitude='-1.234',
    radius='10',
    format='raw',
)

url = 'https://openbenches.org/data.json/&format=raw'
url = 'https://openbenches.org/data.json/?latitude=51.234&longitude=-1.234&radius=20&format=raw'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
data = json.loads(webpage)

benches = data['features']

print(benches)

firstBench = benches[0]

#Find out what requests will be done ---> add fetch by parameters
#Use pico for python server
#Integrate other tree dataset
#Web scraping park info?
