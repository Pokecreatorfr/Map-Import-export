from romh import *
from Value import *

def depoint(point,x):
    hexv = point[x]
    point[x] = hexv[4:6] + hexv [2:4] + hexv[0:2]
