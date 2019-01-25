from urllib.request import Request, urlopen
import json


def getBenches(lat, long, radius):
    lat = str(lat)
    long = str(long)
    radius = str(radius)

    url = 'https://openbenches.org/data.json/' + '?latitude=' + lat + '&longitude=' + \
          long + '&radius=' + radius + '&format=raw'

    req = Request(url)

    webpage = urlopen(req).read()

    data = json.loads(webpage)

    benches = data['features']

    return benches


# getBenches(51.44, -2.587, 500)

