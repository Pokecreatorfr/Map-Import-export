from romh import *
from mape import *
from Value import *
import os
from binascii import unhexlify

filename = "BPRE0.gba"
hexrom = openRomRead(filename)
banktablepointer = readpointer(hexrom, '05524C')
banktablepointer = add2hex(banktablepointer, -4)
#print(banktablepointer)
itsabank = True
while itsabank == True :
    banktablepointer = add2hex(banktablepointer, 4)
    bankpointer = readpointer(hexrom, banktablepointer)
    #print(bankpointer)
    varadr = readpointer(hexrom, banktablepointer)
    varadr = readpointer(hexrom, varadr)
    #print(banktablepointer)
    varhex = readRomData(hexrom, varadr, 28).decode(encoding="utf-8")
    #print(varhex)
    if varhex[6:8] != '08' and varhex[6:8] != '09':
        itsamap = False
    if varhex[14:16] != '08' and  varhex[14:16] != '09' and varhex[14:16] != '00':
        itsamap = False
    if varhex[22:24] != '08' and  varhex[22:24] != '09' and varhex[22:24] != '00':
        itsamap = False
    vardec = conv_hex2dec(varhex[42:44])
    #print(vardec)
    if vardec > 2:
        itsamap = False
    vardec = conv_hex2dec(varhex[44:46])
    if vardec > 15:
        itsamap = False
    vardec = conv_hex2dec(varhex[46:48])
    if vardec > 9:
        itsamap = False
    numbofbank = numbofbank + 1
    if itsapointer == False :
        itsamap = False
    if itsamap == False :
        itsabank = False
    if itsabank == False :
        numbofbank = numbofbank - 1
    if itsabank == True :
        listadre[numbofbank - 1] = banktablepointer
print(listadre)
print('Il y a', str(numbofbank), ' banques de map dans le jeu' )
for i in range (numbofbank):
    vardec3 = 100000000
    varadr = listadre[i]
    varadr = readpointer(hexrom,varadr)
    #print(varhex)
    vardec = conv_hex2dec(varadr)
    for x in range (numbofbank):
        varhex2 = readpointer(hexrom,listadre[x])
        vardec2 = conv_hex2dec(varhex2)
        if vardec < vardec2:
            vardec2 = vardec2 - vardec
        if vardec2 < vardec3 :
            vardec3 = vardec2
        if vardec3 > 800:
            vardec3 = 800
    #print(vardec3)
    #varadr = readpointer(hexrom,varadr)
    varadr = add2hex(varadr, -4)
    itsamap = True
    numbofmap = 0
    vardec4 = 0
    #print(varadr)
    while itsamap == True:
        varadr = add2hex(varadr, 4)
        varadr2 = readpointer(hexrom,varadr)
        #print(varadr)
        varhex = readRomData(hexrom, varadr2, 28).decode(encoding="utf-8")
        #itsamap = False
        if varhex[6:8] != '08' and varhex[6:8] != '09':
            itsamap = False
        if varhex[14:16] != '08' and  varhex[14:16] != '09' and varhex[14:16] != '00':
            itsamap = False
        if varhex[22:24] != '08' and  varhex[22:24] != '09' and varhex[22:24] != '00':
            itsamap = False
        vardec = conv_hex2dec(varhex[42:44])
        #print(vardec)
        if vardec > 2:
            itsamap = False
        vardec = conv_hex2dec(varhex[44:46])
        if vardec > 15:
            itsamap = False
        vardec = conv_hex2dec(varhex[46:48])
        if vardec > 9:
            itsamap = False
        vardec4 = vardec4 + 4
        #print(vardec3,vardec4)
        if vardec4 > vardec3:
            itsamap = False
        numbofmap = numbofmap + 1
        if itsamap == False:
            numbofmap = numbofmap - 1
        nbmap[i] = numbofmap
        #print(varhex)
        #print(itsamap)
        #print(numbofmap)
print(nbmap)

hexrom = openRomRead(filename)
varstr = os.getcwd()
varstr = varstr + '/' + 'maps'
os.mkdir(varstr)
print(varstr)
for i in range(43):
    bankp[i] = readRomData(hexrom, listadre[i], 3)
for x in range(43):
    hexv = bankp[x]
    bankp[x] = hexv[4:6] + hexv [2:4] + hexv[0:2]
    bankp[x] = bankp[x].decode(encoding="utf-8")
    nmap = nbmap[x]
    varstr = os.getcwd()
    varstr2 = varstr + '/maps' + '/' + str(x)
    os.mkdir(varstr2)
    #print(varstr2)
    varstr = os.getcwd()
    varstr = varstr + '/maps' + '/' + str(x)
    for i in range(nmap):
        mapp[i] = conv_hex2dec(bankp[x])+4*i
        mapp[i] = conv_dec2hex(mapp[i])
        hexv = mapp[i]
        #read block
        varadr = readpointer(hexrom,hexv)
        varadr = add2hex(varadr, 16)
        block = readRomData(hexrom, varadr, 12)
        block = block.decode(encoding="utf-8")
        #read largeurh and hauteurh
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        largeurh = readRomData(hexrom, varadr, 4)
        varadr = add2hex(varadr, 4)
        hauteurh = readRomData(hexrom, varadr, 4)
        largeurh = largeurh.decode(encoding="utf-8")
        hauteurh = hauteurh.decode(encoding="utf-8")
        largueurd = conv_hex2dec(largeurh[0:2])
        hauteurd = conv_hex2dec(hauteurh[0:2])
        mapcollseize = largueurd * hauteurd * 2
        varadr = add2hex(varadr, 8)
        varadr = readpointer(hexrom, varadr)
        mapcoll = readRomData(hexrom, varadr, mapcollseize)
        mapcoll = mapcoll.decode(encoding="utf-8")
        # Read tileset informations*
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        varadr = add2hex(varadr, 16)
        varadr2 = readpointer(hexrom, varadr)
        vardec2 = conv_hex2dec(varadr2)
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        varadr = add2hex(varadr, 20)
        varadr3 = readpointer(hexrom, varadr)
        vardec3 = conv_hex2dec(varadr3)
        tileset1d = (vardec2 - tilesetstart) / 24
        tileset2d = (vardec3 - tilesetstart) / 24
        varhex2 = conv_dec2hex(int(tileset1d))
        varhex3 = conv_dec2hex(int(tileset2d))
        if len(varhex2) == 1:
            varhex2 = "0" + varhex2
        if len(varhex3) == 1:
            varhex3 = "0" + varhex3
        tileset1 = varhex2 + "000000"
        tileset2 = varhex3 + "000000"
        #Read bodure block informations
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        varadr = add2hex(varadr, 24)
        largbordh = readRomByte(hexrom, varadr)
        largbordh = largbordh.decode(encoding="utf-8")
        largbordd = conv_hex2dec(largbordh)
        varadr = add2hex(varadr, 1)
        hautbordh = readRomByte(hexrom, varadr)
        hautbordh= hautbordh.decode(encoding="utf-8")
        hautbordd = conv_hex2dec(hautbordh)
        size = (hautbordd * largbordd) * 2
        #Read bodure block
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        varadr = add2hex(varadr, 8)
        varadr = readpointer(hexrom, varadr)
        blockbord = readRomData(hexrom, varadr, size).decode(encoding="utf-8")
        #Read event
        varadr = readpointer(hexrom, hexv)
        varadr = add2hex(varadr, 4)
        varadr = readpointer(hexrom, varadr)
        pnjscripth = readRomByte(hexrom, varadr)
        varadr = add2hex(varadr, 1)
        warph = readRomByte(hexrom, varadr)
        varadr = add2hex(varadr, 1)
        scripth = readRomByte(hexrom, varadr)
        varadr = add2hex(varadr, 1)
        pancarteh = readRomByte(hexrom, varadr)
        pnjscripth = pnjscripth.decode(encoding="utf-8")
        warph = warph.decode(encoding="utf-8")
        scripth = scripth.decode(encoding="utf-8")
        pancarteh = pancarteh.decode(encoding="utf-8")
        pnjscriptd = conv_hex2dec(pnjscripth)
        warpd = conv_hex2dec(warph)
        scriptd = conv_hex2dec(scripth)
        pancarted = conv_hex2dec(pancarteh)
        varadr = add2hex(varadr, 1)
        varadr2 = readpointer(hexrom, varadr)
        sizepnj = pnjscriptd * 24
        varhex2 = readRomData(hexrom, varadr2, sizepnj)
        varhex2 = varhex2.decode(encoding="utf-8")
        mapevent = varhex2
        varadr = add2hex(varadr, 4)
        varadr2 = readpointer(hexrom, varadr)
        sizewarp = warpd * 8
        varhex2 = readRomData(hexrom, varadr2, sizewarp)
        varhex2 = varhex2.decode(encoding="utf-8")
        mapevent = mapevent + varhex2
        sizescript = scriptd * 16
        varadr = add2hex(varadr, 4)
        varadr2 = readpointer(hexrom, varadr)
        varhex2 = readRomData(hexrom, varadr2, sizescript)
        varhex2 = varhex2.decode(encoding="utf-8")
        mapevent = mapevent + varhex2
        sizepancarte = pancarted * 12
        varadr = add2hex(varadr, 4)
        varadr2 = readpointer(hexrom, varadr)
        varhex2 = readRomData(hexrom, varadr2, sizepancarte)
        varhex2 = varhex2 = varhex2.decode(encoding="utf-8")
        mapevent = mapevent + varhex2
        mapevent = mapevent + pnjscripth + warph + scripth + pancarteh
        # Read connection informations
        varadr = readpointer(hexrom, hexv)
        varadr = add2hex(varadr, 12)
        varadr = readpointer(hexrom, varadr)
        if varadr != "000000":
            #print(varadr)
            connectionh = readRomData(hexrom, varadr, 4)
            connectionh = connectionh.decode(encoding="utf-8")
            connectiond = conv_hex2dec(connectionh[0:2])
            size = connectiond * 12
            varadr = add2hex(varadr, 4)
            varadr = readpointer(hexrom, varadr)
            mapconnections = readRomData(hexrom, varadr, size)
            mapconnections = mapconnections.decode(encoding="utf-8")
            mapconnections = mapconnections + connectionh
        else :
            mapconnections = "0000"
        #build map file
        mapfilepart1 = largeurh + hauteurh + tileset1 + tileset2 + largbordh + hautbordh + 'c300'+ GC + '34000000'
        mapfilepart2 = block + blockbord + mapcoll
        mapfilepart3 = mapevent
        vardec2 = len(mapfilepart1) - 2 + 24 + len(mapfilepart2) + len(mapfilepart3)
        vardec2 = vardec2/2
        vardec2 = int(vardec2) - 3
        varhex2 = conv_dec2hex(vardec2)
        if len(varhex2) == 3 :
            varhex2 = '0' + varhex2
        if len(varhex2) == 2 :
            varhex2 = '00' + varhex2
        varhex2 = varhex2[2:4] + varhex2[0:2] + '0000'
        mapfilepart1 = mapfilepart1 + varhex2 + '00000000'
        vardec2 = len(mapfilepart1) - 2 + 8 + len(mapfilepart2)
        vardec2 = vardec2/2
        vardec2 = vardec2 + 1
        vardec2 = int(vardec2)
        varhex2 = conv_dec2hex(vardec2)
        if len(varhex2) == 3 :
            varhex2 = '0' + varhex2
        if len(varhex2) == 2 :
            varhex2 = '00' + varhex2
        varhex2 = varhex2[2:4] + varhex2[0:2] + '0000'
        mapfilepart3 = mapfilepart3 + varhex2
        vardec2 = vardec2 + sizepnj
        varhex2 = conv_dec2hex(vardec2)
        if len(varhex2) == 3 :
            varhex2 = '0' + varhex2
        if len(varhex2) == 2 :
            varhex2 = '00' + varhex2
        varhex2 = varhex2[2:4] + varhex2[0:2] + '0000'
        mapfilepart3 = mapfilepart3 + varhex2
        vardec2 = vardec2 + sizewarp
        varhex2 = conv_dec2hex(vardec2)
        if len(varhex2) == 3 :
            varhex2 = '0' + varhex2
        if len(varhex2) == 2 :
            varhex2 = '00' + varhex2
        varhex2 = varhex2[2:4] + varhex2[0:2] + '0000'
        mapfilepart3 = mapfilepart3 + varhex2
        vardec2 = vardec2 + sizescript
        varhex2 = conv_dec2hex(vardec2)
        if len(varhex2) == 3 :
            varhex2 = '0' + varhex2
        if len(varhex2) == 2 :
            varhex2 = '00' + varhex2
        varhex2 = varhex2[2:4] + varhex2[0:2] + '0000'
        mapfilepart3 = mapfilepart3 + varhex2
        vardec2 = len(mapfilepart1) - 2 + 8 + len(mapfilepart2) + len(mapfilepart3)
        vardec2 = vardec2/2
        vardec2 = vardec2 + 1
        vardec2 = int(vardec2)
        varhex2 = conv_dec2hex(vardec2)
        if len(varhex2) == 3 :
            varhex2 = '0' + varhex2
        if len(varhex2) == 2 :
            varhex2 = '00' + varhex2
        varhex2 = varhex2[2:4] + varhex2[0:2] + '0000'
        mapconnections = mapconnections + varhex2
        mapfilepart3 = mapfilepart3 + mapconnections
        vardec2 = len(mapfilepart1) - 2 + 8 + len(mapfilepart2) + len(mapfilepart3)
        vardec2 = vardec2/2
        vardec2 = vardec2 + 1 - 8
        vardec2 = int(vardec2)
        varhex2 = conv_dec2hex(vardec2)
        if len(varhex2) == 3 :
            varhex2 = '0' + varhex2
        if len(varhex2) == 2 :
            varhex2 = '00' + varhex2
        varhex2 = varhex2[2:4] + varhex2[0:2] + '0000'
        mapfilefinal = mapfilepart1 + varhex2 + mapfilepart2 + mapfilepart3
        mapfilefinal = unhexlify(mapfilefinal)
        varstr2 = varstr + '/' + str(i) + '.map'
        varstr2 = str(varstr2)
        mapfile = open(varstr2,'wb')
        mapfile.write(mapfilefinal)
        mapfile.close()
        print(varstr2)

    #print(mapp)
    #print(bankp)
#print(bankp)
#print(mapp)
