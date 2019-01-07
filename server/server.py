import pico
from pico import PicoApp

import parks
import trees
import benches


def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'OPTIONS':
        start_response(
            '200 OK',
            [
                ('Content-Type', 'application/json'),
                ('Access-Control-Allow-Origin', '*'),
                ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
                ('Access-Control-Allow-Methods', 'POST'),
            ]
        )
        return ''


@pico.expose()
def getPark(code):
    return parks.getPark(code)


@pico.expose()
def getAllParkNames():
    return parks.getAllParkNames()


@pico.expose()
def getNearestParks(lat, long):
    return parks.getNearestParks(lat, long)


@pico.expose()
def getTrees(siteCode, lat, long):
    return trees.getTrees(siteCode, lat, long)


@pico.expose()
def getBenches(lat, long, radius):
    return benches.getBenches(lat, long, radius)


app = PicoApp()
app.register_module(__name__)
