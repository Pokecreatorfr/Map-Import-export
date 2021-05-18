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
        noconnection = False
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
        bordure = readRomData(mapfilefinal , '34' , size)
        varhex = add2hex('34', size)
        mapcollseize = largueurd * hauteurd * 2
        mapcoll = readRomData(mapfilefinal ,varhex, mapcollseize).decode(encoding="utf-8")
        vardec = len(mapfilefinal)
        varadr = mapfilefinal.decode(encoding="utf-8")[74:76] + mapfilefinal.decode(encoding="utf-8")[72:74]
        connectionh = readRomByte(mapfilefinal,varadr).decode(encoding="utf-8")
        connectiond = conv_hex2dec(connectionh)
        varadr = add2hex(varadr,4)
        varadr = readRomData(mapfilefinal, varadr, 2).decode(encoding="utf-8")
        varadr = varadr[2:4] +varadr[0:2]
        connexions = readRomData(mapfilefinal, varadr, connectiond*12).decode(encoding="utf-8")
        #print(mapcoll)
        #print(varadr)
        #print(connexions)
        if connexions == '':
            noconnection = True
        varadr = readRomData(mapfilefinal,'1C', 2).decode(encoding="utf-8")
        varadr = varadr[2:4] + varadr[0:2]
        #print(varadr)
        pnjscripth = readRomByte(mapfilefinal, varadr).decode(encoding="utf-8")
        warph = readRomByte(mapfilefinal, add2hex(varadr, 1)).decode(encoding="utf-8")
        scripth = readRomByte(mapfilefinal, add2hex(varadr, 2)).decode(encoding="utf-8")
        pancarteh = readRomByte(mapfilefinal, add2hex(varadr, 3)).decode(encoding="utf-8")
        pnjscriptd = conv_hex2dec(pnjscripth)
        warpd = conv_hex2dec(warph)
        scriptd = conv_hex2dec(scripth)
        pancarted = conv_hex2dec(pancarteh)
        #print(pnjscriptd, warpd, scriptd, pancarted)
        varadr2 = readRomData(mapfilefinal, add2hex(varadr,4), 4).decode(encoding="utf-8")
        varadr2 = varadr[6:8] + varadr[4:6] +varadr[2:4] + varadr[0:2]
        pnjscript = readRomData(mapfilefinal,varadr2, pnjscriptd*24)
        varadr2 = readRomData(mapfilefinal, add2hex(varadr,8), 4).decode(encoding="utf-8")
        varadr2 = varadr[6:8] + varadr[4:6] +varadr[2:4] + varadr[0:2]
        warp = readRomData(mapfilefinal,varadr2, warpd*8)
        varadr2 = readRomData(mapfilefinal, add2hex(varadr,12), 4).decode(encoding="utf-8")
        varadr2 = varadr[6:8] + varadr[4:6] +varadr[2:4] + varadr[0:2]
        script = readRomData(mapfilefinal,varadr2, scriptd*16)
        varadr2 = readRomData(mapfilefinal, add2hex(varadr,16), 4).decode(encoding="utf-8")
        varadr2 = varadr[6:8] + varadr[4:6] +varadr[2:4] + varadr[0:2]
        pancarte = readRomData(mapfilefinal,varadr2, pancarted*12)
        varadr3 = conv_dec2hex(int(hexrom.find(bordure)/2))
        if varadr3 != '0':
            varadr3 = unhexlify(makepointer(varadr3))
            maptable1 = unhexlify(largeurh) + unhexlify(hauteurh) + varadr3
        else :
            varadr3 = conv_dec2hex(search(hexrom, len(bordure)/2, 00))
            writedatainrom(filename, bordure, varadr3)
        print(varadr3)
        #print(mapcoll)
        #print(noconnection)
