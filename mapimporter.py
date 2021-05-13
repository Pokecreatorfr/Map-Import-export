from romh import *
from mape import *
from Value import *
import os
from binascii import unhexlify

varstr = os.getcwd() + '/maps'
numbofbank = (len(next(os.walk(varstr))[1]))
for i in range(numbofbank):
    varstr2 = varstr + '/' + str(i)
    path, dirs, files = next(os.walk(varstr2))
    nbmap[i] = len(files)

filename = "BPRE0.gba"
for i in range(numbofbank):
    hexrom = openRomRead(filename)
    varstr = os.getcwd()
    varstr = varstr + '/' + 'maps' + '/' + str(i)
    #print(varstr)
    nmap = nbmap[i]
    for x in range(nmap):
        hexrom = openRomRead(filename)
        varstr2 = varstr + '/' + str(x) + '.map'
        print(varstr2)
        mapfilefinal = openRomRead(varstr2)
        largeurh = readRomData(mapfilefinal ,'00', 4).decode(encoding="utf-8")
        largueurd = conv_hex2dec(largeurh[0:2])
        hauteurh = readRomData(mapfilefinal ,'04', 4).decode(encoding="utf-8")
        hauteurd = conv_hex2dec(hauteurh[0:2])
        tileset1 = readRomData(mapfilefinal ,'08', 4).decode(encoding="utf-8")
        tileset2 = readRomData(mapfilefinal ,'0C', 4).decode(encoding="utf-8")
        largbordh = readRomByte(mapfilefinal, '10').decode(encoding="utf-8")
        largbordd = conv_hex2dec(largbordh)
        hautbordh = readRomByte(mapfilefinal, '11').decode(encoding="utf-8")
        hautbordd = conv_hex2dec(hautbordh)
        size = (hautbordd * largbordd) * 2
        block = readRomData(mapfilefinal , '28' , 12).decode(encoding="utf-8")
        bordure = readRomData(mapfilefinal , '34' , size).decode(encoding="utf-8")
        varhex = add2hex('34', size+1)
        mapcollseize = largueurd * hauteurd * 2
        mapcoll = readRomData(mapfilefinal ,varhex, mapcollseize).decode(encoding="utf-8")
        print(varstr2)
        print(mapcoll)
