from romh import *
from mape import *
from Value import *
import os
from binascii import unhexlify
from binascii import hexlify

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
    numbofbankinrom = numbofbankinrom + 1
    if itsapointer == False :
        itsamap = False
    if itsamap == False :
        itsabank = False
    if itsabank == False :
        numbofbankinrom = numbofbankinrom - 1
    if itsabank == True :
        listadre[numbofbankinrom - 1] = banktablepointer
print(listadre)
print('Il y a', str(numbofbankinrom), ' banques de map dans le jeu' )
for i in range (numbofbankinrom):
    vardec3 = 100000000
    varadr = listadre[i]
    varadr = readpointer(hexrom,varadr)
    #print(varhex)
    vardec = conv_hex2dec(varadr)
    for x in range (numbofbankinrom):
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
        print(vardec3,vardec4)
        if vardec4 > vardec3:
            itsamap = False
        numbofmap = numbofmap + 1
        if itsamap == False:
            numbofmap = numbofmap - 1
        nbmapinrom[i] = numbofmap
        print(varhex)
        print(itsamap)
        #print(numbofmap)
    print(nbmapinrom)
print(listadre)
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
    mapstable = ''
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
        mapcoll = readRomData(mapfilefinal ,varhex, mapcollseize)
        vardec = len(mapfilefinal)
        varadr = mapfilefinal.decode(encoding="utf-8")[74:76] + mapfilefinal.decode(encoding="utf-8")[72:74]
        connectionh = readRomByte(mapfilefinal,varadr).decode(encoding="utf-8")
        print(connectionh)
        connectiond = conv_hex2dec(connectionh)
        varadr = add2hex(varadr,4)
        varadr = readRomData(mapfilefinal, varadr, 2).decode(encoding="utf-8")
        varadr = varadr[2:4] +varadr[0:2]
        connexions = readRomData(mapfilefinal, varadr, connectiond*12)
        print(connexions)
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
        varadr2 = varadr2[6:8] + varadr2[4:6] +varadr2[2:4] + varadr2[0:2]
        pnjscript = readRomData(mapfilefinal,varadr2, pnjscriptd*24)
        varadr2 = readRomData(mapfilefinal, add2hex(varadr,8), 4).decode(encoding="utf-8")
        varadr2 = varadr2[6:8] + varadr2[4:6] +varadr2[2:4] + varadr2[0:2]
        warp = readRomData(mapfilefinal,varadr2, warpd*8)
        varadr2 = readRomData(mapfilefinal, add2hex(varadr,12), 4).decode(encoding="utf-8")
        varadr2 = varadr2[6:8] + varadr2[4:6] +varadr2[2:4] + varadr2[0:2]
        script = readRomData(mapfilefinal,varadr2, scriptd*16)
        varadr2 = readRomData(mapfilefinal, add2hex(varadr,16), 4).decode(encoding="utf-8")
        varadr2 = varadr2[6:8] + varadr2[4:6] +varadr2[2:4] + varadr2[0:2]
        pancarte = readRomData(mapfilefinal,varadr2, pancarted*12)
        varadr3 = searchdatainrom(hexrom, bordure)
        if conv_hex2dec(varadr3) % 2 != 0 & conv_hex2dec(varadr3) != 0:
            print('ATTENTION MATHEO TU AS FAIT DE LA MERDE !!!!!')
        if varadr3 != '0':
            #print(varadr3)
            varadr3 = unhexlify(makepointer(varadr3))
            maptable1 = unhexlify(largeurh) + unhexlify(hauteurh) + varadr3
        else :
            varadr3 = searchdatainrom(hexrom,freebyte(int(len(bordure)/2)))
            writedatainrom(filename, bordure, varadr3)
            hexrom = openRomRead(filename)
            varadr3 = unhexlify(makepointer(varadr3))
            maptable1 = unhexlify(largeurh) + unhexlify(hauteurh) + varadr3
        varadr3 = searchdatainrom(hexrom, mapcoll)
        #print(varadr3)
        if varadr3 != '0':
            varadr3 = unhexlify(makepointer(varadr3))
            maptable1 = maptable1 + varadr3
        else :
            varadr3 = searchdatainrom(hexrom, freebyte(int(len(mapcoll)/2)))
            writedatainrom(filename, mapcoll, varadr3)
            hexrom = openRomRead(filename)
            varadr3 = unhexlify(makepointer(varadr3))
            maptable1 = maptable1 + varadr3
        tileset1 = mapfilefinal[22:24] + mapfilefinal[20:22] + mapfilefinal[18:20] + mapfilefinal[16:18]
        tileset2 = mapfilefinal[30:32] + mapfilefinal[28:30] + mapfilefinal[26:28] + mapfilefinal[24:26]
        tileset1 = tileset1.decode(encoding="utf-8")
        tileset2 = tileset2.decode(encoding="utf-8")
        tileset1d = conv_hex2dec(tileset1)*24 +tilesetstart
        tileset2d = conv_hex2dec(tileset2)*24 +tilesetstart
        print(conv_hex2dec(tileset2),tileset2,tilesetstart,tileset2d)
        tileset1 = conv_dec2hex(tileset1d)
        tileset2 = conv_dec2hex(tileset2d)
        tileset1 = makepointer(tileset1)
        print(tileset2)
        tileset2 = makepointer(tileset2)
        maptable1 = maptable1 + unhexlify(tileset1) + unhexlify(tileset2) + unhexlify(mapfilefinal[32:34]) + unhexlify(mapfilefinal[34:36]) + unhexlify('0000')
        maptable1 = hexlify(maptable1)
        if x <= nbmapinrom[i]:
            varadr3 = readpointer(hexrom, listadre[i])
            #print(listadre[i], varadr3, add2hex(varadr3, 4*x))
            varadr3 = readpointer(hexrom, add2hex(varadr3, 4*x))
            #print(varadr3)
            varadr3 = readpointer(hexrom, varadr3)
            #print(varadr3)
            writedatainrom(filename, maptable1, varadr3)
        else:
            varadr3 = searchdatainrom(hexrom, freebyte(28))
            writedatainrom(filename, maptable1, varadr3)
        hexrom = openRomRead(filename)
        maptable2 = makepointer(varadr3)
        #print(warph, scripth, pancarteh, pnjscripth)
        if warph == '00' and scripth == '00' and pancarteh == '00' and pnjscripth =='00':
            maptable1 = '0000000000000000000000000000000000000000'
        else:
            maptable1 = pnjscripth + warph + scripth + pancarteh
            if pnjscripth == '00':
                maptable1 = maptable1 + '00000000'
            else :
                varadr3 = searchdatainrom(hexrom , pnjscript)
                if varadr3 != '0':
                    varadr3 = makepointer(varadr3)
                else :
                    varadr3 = searchdatainrom(hexrom,freebyte(int(len(pnjscript)/2)))
                    writedatainrom(filename, pnjscript, varadr3)
                    hexrom = openRomRead(filename)
                    varadr3 = makepointer(varadr3)
                maptable1 = maptable1 + varadr3
            if warph == '00':
                maptable1 = maptable1 + '00000000'
            else :
                varadr3 = searchdatainrom(hexrom , warp)
                if varadr3 != '0':
                    varadr3 = makepointer(varadr3)
                else :
                    varadr3 = searchdatainrom(hexrom ,freebyte(int(len(warp)/2)))
                    writedatainrom(filename, warp, varadr3)
                    hexrom = openRomRead(filename)
                    varadr3 = makepointer(varadr3)
                maptable1 = maptable1 + varadr3
            if scripth == '00':
                maptable1 = maptable1 + '00000000'
            else :
                varadr3 = searchdatainrom(hexrom , script)
                if varadr3 != '0':
                    varadr3 = makepointer(varadr3)
                else :
                    varadr3 = searchdatainrom(hexrom,freebyte(int(len(script)/2)))
                    writedatainrom(filename, script, varadr3)
                    hexrom = openRomRead(filename)
                    varadr3 = makepointer(varadr3)
                maptable1 = maptable1 + varadr3
            if pancarteh == '00':
                maptable1 = maptable1 + '00000000'
            else :
                varadr3 = searchdatainrom(hexrom ,pancarte)
                if varadr3 != '0':
                    varadr3 = makepointer(varadr3)
                else :
                    varadr3 = searchdatainrom(hexrom, freebyte(int(len(pancarte)/2)))
                    writedatainrom(filename, pancarte, varadr3)
                    hexrom = openRomRead(filename)
                    varadr3 = makepointer(varadr3)
                maptable1 = maptable1 + varadr3
        if x <= nbmapinrom[i]:
            varadr3 = readpointer(hexrom, listadre[i])
            varadr3 = readpointer(hexrom, add2hex(varadr3, 4*x))
            varadr3 = readpointer(hexrom, add2hex(varadr3,4))
            writedatainrom(filename, maptable1, varadr3)
        else:
            varadr3 = conv_dec2hex(int(search(filename, 20, 00)))
            writedatainrom(filename, maptable1, varadr3)
        hexrom = openRomRead(filename)
        maptable2 = maptable2 + makepointer(varadr3)
        varadr3 = conv_dec2hex(int(hexrom[8388608:].find(hexlify(unhexlify('ffffffff')))/2))
        varadr3 = add2hex(varadr3, 8388608)
        writedatainrom(filename, '00ff', varadr3)
        hexrom = openRomRead(filename)
        maptable2 = maptable2 + makepointer(varadr3)
        #print(connexions)
        if connectiond == 0:
            varadr3 = '00000000'
        else:
            varhex = connexions
            #print(varhex)
            varadr3 = searchdatainrom(hexrom , varhex)
            if varadr3 != '0':
                varadr3 = makepointer(varadr3)
            else :
                varhex = 'ff' * int(len(connexions))
                varadr3 = conv_dec2hex(int(hexrom[8388608:].find(hexlify(unhexlify(varhex)))/2))
                varadr3 = add2hex(varadr3, 8388608)
                writedatainrom(filename, connexions, varadr3)
                hexrom = openRomRead(filename)
                varadr3 = makepointer(varadr3)
            maptable1 = connectionh + '000000' + varadr3
            if x <= nbmapinrom[i]:
                varadr3 = readpointer(hexrom, listadre[i])
                varadr3 = readpointer(hexrom, add2hex(varadr3, 4*x))
                varadr3 = readpointer(hexrom, add2hex(varadr3,12))
                writedatainrom(filename, maptable1, varadr3)
            else:
                varadr3 = conv_dec2hex(int(search(filename, 10, 00)))
                writedatainrom(filename, maptable1, varadr3)
            varadr3 = makepointer(varadr3)
        maptable2 = maptable2 + varadr3 + block
        #print(maptable2, block)
        if x <= nbmapinrom[i]:
            varadr3 = readpointer(hexrom, listadre[i])
            varadr3 = readpointer(hexrom, add2hex(varadr3, 4*x))
            writedatainrom(filename, maptable2, varadr3)
        else:
            varadr3 = conv_dec2hex(int(search(filename, 28, 00)))
            writedatainrom(filename, maptable2, varadr3)
        mapstable = mapstable + makepointer(varadr3)
    if nbmap[i] <= nbmapinrom[i]:
        mapstable = mapstable + "ffffffff" * (nbmapinrom[i] - nbmap[i])
        varadr3 = readpointer(hexrom, listadre[i])
        writedatainrom(filename, mapstable, varadr3)
    else:
        varadr3 = searchdatainrom(hexrom,freebyte(int(len(mapstable)/2)))
        writedatainrom(filename, mapstable, varadr3)
    banktable = banktable + makepointer(varadr3)
if numbofbank <= numbofbankinrom:
    banktable = banktable + "ffffffff" * (numbofbankinrom - numbofbank)
    #print(banktable, len(banktable))
    writedatainrom(filename, banktable, listadre[0])
else:
    varadr3 = varadr3 = conv_dec2hex(int(search(filename, len(banktable)/2, 00)))
    writedatainrom(filename, banktable, varadr3)
print('────────▄███████████▄────────')
print('─────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────')
print('────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────')
print('───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───')
print('──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──')
print('██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██')
print('██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██')
print('██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██')
print('███████████░░███░░███████████')
print('██░░░░░░░██░░███░░██░░░░░░░██')
print('██░░░░░░░░██░░░░░██░░░░░░░░██')
print('██░░░░░░░░░███████░░░░░░░░░██')
print('─██░░░░░░░░░░░░░░░░░░░░░░░██─')
print('──██░░░░░░░░░░░░░░░░░░░░░██──')
print('───██░░░░░░░░░░░░░░░░░░░██───')
print('────███░░░░░░░░░░░░░░░███────')
print('─────▀███░░░░░░░░░░░███▀─────')
print('────────▀███████████▀────────')
print('##################################\n Map importation: finished. Congratulation.\n Scripts made by Pokecreatorfr with the help of some members of Pokémon Trash,\n and has the help of HexManiacAdvence, http://datacrystal.romhacking.net \n and by python library made by cosarara97.\n If you encounter any bugs please contact pokecreatorfr.\n##################################')
