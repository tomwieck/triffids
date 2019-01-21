# import urllib, json
# from urllib.request import Request, urlopen
# import json
# import urllib


# def getBenches(lat, long, radius):
#     lat = str(lat)
#     long = str(long)
#     radius = str(radius)

#     url = 'https://openbenches.org/data.json/' + '?latitude=' + lat + '&longitude=' +
#           long + '&radius=' + radius + '&format=raw'

#     req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

#     webpage = urlopen(req).read()

#     data = json.loads(webpage)

#     benches = data['features']
#     #print(benches)
#     return benches


# getBenches(51.234, -1.234, 20)

