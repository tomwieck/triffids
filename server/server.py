
import pico
from pico import PicoApp

import parks
import trees
import benches

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