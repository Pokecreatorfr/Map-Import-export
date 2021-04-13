from romh import *
from Value import *

def depointbank(x):
    hexv = bankp[x]
    bankp[x] = hexv[4:6] + hexv [2:4] + hexv[0:2]
