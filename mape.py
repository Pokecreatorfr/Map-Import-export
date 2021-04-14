from romh import *

def depointl(point,x):
    hexv = point[x]
    point[x] = hexv[4:6] + hexv [2:4] + hexv[0:2]

def ajouthexl(list,x,y):
    for i in range(x):
        hexv = conv_hex2dec(list[x])+y
        list[x] = conv_dec2hex(hexv)
