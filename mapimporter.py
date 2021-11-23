import os
from binascii import hexlify, unhexlify

from mape import *
from romh import *
from Value import *

filename = "BPRE0.gba"
bankend = False
hexrom = openRomRead(filename)
banktablepointer = readpointer(hexrom, '05524C')
banktablepointer = add2hex(banktablepointer, -4)
# print(banktablepointer)
itsabank = True
while itsabank == True:
    banktablepointer = add2hex(banktablepointer, 4)
    bankpointer = readpointer(hexrom, banktablepointer)
    # print(bankpointer)
    varadr = readpointer(hexrom, banktablepointer)
    varadr = readpointer(hexrom, varadr)
    # print(banktablepointer)
    varhex = readRomData(hexrom, varadr, 28).decode(encoding="utf-8")
    # print(varhex)
    if varhex[6:8] != '08' and varhex[6:8] != '09':
        itsamap = False
    if varhex[14:16] != '08' and varhex[14:16] != '09' and varhex[14:16] != '00':
        itsamap = False
    if varhex[22:24] != '08' and varhex[22:24] != '09' and varhex[22:24] != '00':
        itsamap = False
    vardec = conv_hex2dec(varhex[42:44])
    # print(vardec)
    if vardec > 2:
        itsamap = False
    vardec = conv_hex2dec(varhex[44:46])
    if vardec > 15:
        itsamap = False
    vardec = conv_hex2dec(varhex[46:48])
    if vardec > 9:
        itsamap = False
    numbofbankinrom = numbofbankinrom + 1
    if itsapointer == False:
        itsamap = False
    if itsamap == False:
        itsabank = False
    if itsabank == False:
        numbofbankinrom = numbofbankinrom - 1
    if itsabank == True:
        listadre[numbofbankinrom - 1] = banktablepointer
# print(listadre)
#print('Il y a', str(numbofbankinrom), ' banques de map dans le jeu')
for i in range(numbofbankinrom):
    vardec3 = 100000000
    varadr = listadre[i]
    varadr = readpointer(hexrom, varadr)
    # print(varhex)
    vardec = conv_hex2dec(varadr)
    for x in range(numbofbankinrom):
        varhex2 = readpointer(hexrom, listadre[x])
        vardec2 = conv_hex2dec(varhex2)
        if vardec < vardec2:
            vardec2 = vardec2 - vardec
        if vardec2 < vardec3:
            vardec3 = vardec2
        if vardec3 > 800:
            vardec3 = 800
    # print(vardec3)
    #varadr = readpointer(hexrom,varadr)
    varadr = add2hex(varadr, -4)
    itsamap = True
    numbofmap = 0
    vardec4 = 0
    # print(varadr)
    while itsamap == True:
        varadr = add2hex(varadr, 4)
        varadr2 = readpointer(hexrom, varadr)
        # print(varadr)
        varhex = readRomData(hexrom, varadr2, 28).decode(encoding="utf-8")
        #itsamap = False
        if varhex[6:8] != '08' and varhex[6:8] != '09':
            itsamap = False
        if varhex[14:16] != '08' and varhex[14:16] != '09' and varhex[14:16] != '00':
            itsamap = False
        if varhex[22:24] != '08' and varhex[22:24] != '09' and varhex[22:24] != '00':
            itsamap = False
        vardec = conv_hex2dec(varhex[42:44])
        # print(vardec)
        if vardec > 2:
            itsamap = False
        vardec = conv_hex2dec(varhex[44:46])
        if vardec > 15:
            itsamap = False
        vardec = conv_hex2dec(varhex[46:48])
        if vardec > 9:
            itsamap = False
        vardec4 = vardec4 + 4
        #print(vardec3, vardec4)
        if vardec4 > vardec3:
            itsamap = False
        numbofmap = numbofmap + 1
        if itsamap == False:
            numbofmap = numbofmap - 1
        nbmapinrom[i] = numbofmap
        # print(varhex)
        # print(itsamap)
        # print(numbofmap)
    # print(nbmapinrom)
# print(listadre)
varstr = os.getcwd() + '/maps'
numbofbank = (len(next(os.walk(varstr))[1]))
for i in range(numbofbank):
    varstr2 = varstr + '/' + str(i)
    path, dirs, files = next(os.walk(varstr2))
    nbmap[i] = len(files)
print('Il y a', str(numbofbankinrom), ' banques de map dans le jeu')

filename = "BPRE0.gba"
hexrom = openRomRead(filename).decode(encoding="utf-8")
bankstable = ''
for i in range(numbofbank):
    varstr = os.getcwd()
    varstr = varstr + '/' + 'maps' + '/' + str(i)
    print(varstr)
    nmap = nbmap[i]
    banktable = ''
    for x in range(nmap):
        varstr2 = varstr + '/' + str(x) + '.map'
        print(varstr2)
        noconnection = False
        mapfilefinal = openRomRead(varstr2)
        # mapA corresponbd à la map Actuelle
        mapA = mapformat(mapfilefinal)
        # Construction de maptable1
        maptable1 = mapA.largeurhex + mapA.hauteurhex
        varadr = searchdatainrom(hexrom, 'f' * len(mapA.blockbord))
        hexrom = write_in_hex_string(hexrom, varadr, mapA.blockbord)
        maptable1 = maptable1 + makepointer(varadr)
        varadr = searchdatainrom(hexrom, 'f' * len(mapA.mapcoll))
        hexrom = write_in_hex_string(hexrom, varadr, mapA.mapcoll)
        maptable1 = maptable1 + makepointer(varadr) + makepointer(conv_dec2hex(mapA.tileset1dec * 24 + tilesetstart)) + makepointer(
            conv_dec2hex(mapA.tileset2dec * 24 + tilesetstart)) + mapfilefinal[32:36].decode(encoding="utf-8") + '0000'
        # Construction de scripttable
        if mapA.nbwarp == '00' and mapA.nbscript == '00' and mapA.nbpancarte == '00' and mapA.nbscriptpnj == '00':
            scripttable = '0000000000000000000000000000000000000000'
        else:
            scripttable = mapA.nbscriptpnj + mapA.nbwarp + mapA.nbscript + mapA.nbpancarte
            if mapA.nbscriptpnj == '00':
                scripttable = scripttable + '00000000'
            else:
                varadr = searchdatainrom(hexrom, 'f' * len(mapA.scriptpnj))
                hexrom = write_in_hex_string(hexrom, varadr, mapA.scriptpnj)
                scripttable = scripttable + makepointer(varadr)
            if mapA.nbwarp == '00':
                scripttable = scripttable + '00000000'
            else:
                varadr = searchdatainrom(hexrom, 'f' * len(mapA.warp))
                hexrom = write_in_hex_string(hexrom, varadr, mapA.warp)
                scripttable = scripttable + makepointer(varadr)
            if mapA.nbscript == '00':
                scripttable = scripttable + '00000000'
            else:
                varadr = searchdatainrom(hexrom, 'f' * len(mapA.script))
                hexrom = write_in_hex_string(hexrom, varadr, mapA.script)
                scripttable = scripttable + makepointer(varadr)
            if mapA.nbpancarte == '00':
                scripttable = scripttable + '00000000'
            else:
                varadr = searchdatainrom(hexrom, 'f' * len(mapA.pancarte))
                hexrom = write_in_hex_string(hexrom, varadr, mapA.pancarte)
                scripttable = scripttable + makepointer(varadr)
        # Construction de conexiontable
        if mapA.noconnexion == False:
            varadr = searchdatainrom(hexrom, 'f' * (len(mapA.connexion)+4))
            hexrom = write_in_hex_string(hexrom,varadr, mapA.connexion +
                                makepointer(varadr))
            connexiontable = makepointer(
                add2hex(varadr, int(len(mapA.connexion)/2) - 4))
        # Création de la table de la map
        varadr = searchdatainrom(hexrom, 'f' * len(maptable1))
        hexrom = write_in_hex_string(hexrom,varadr, maptable1)
        mapstable = makepointer(varadr)
        varadr = searchdatainrom(hexrom, 'f' * len(scripttable))
        hexrom = write_in_hex_string(hexrom,varadr, scripttable)
        mapstable = mapstable + makepointer(varadr)
        varadr = searchdatainrom(hexrom, '00000000')
        mapstable = mapstable + makepointer(varadr)
        if mapA.noconnexion == False:
            varadr = searchdatainrom(hexrom, 'f' * len(connexiontable))
            hexrom = write_in_hex_string(hexrom,varadr, connexiontable)
            mapstable = mapstable + makepointer(varadr) + mapA.block
        else:
            mapstable = mapstable + '00000000' + mapA.block
        varadr = searchdatainrom(hexrom, 'f' * len(mapstable))
        hexrom = write_in_hex_string(hexrom,varadr, mapstable)
        banktable = banktable + makepointer(varadr)
    varadr = searchdatainrom(hexrom, 'f' * len(banktable))
    hexrom = write_in_hex_string(hexrom,varadr, banktable)
    bankstable = bankstable + makepointer(varadr)
varadr = searchdatainrom(hexrom, 'f' * len(bankstable))
hexrom = write_in_hex_string(hexrom,varadr, bankstable)
#hexrom = write_in_hex_string(hexrom, '05524C', makepointer(varadr))


with open("test.gba", "wb") as f:
    f.write(unhexlify(hexrom))
    f.close()


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
