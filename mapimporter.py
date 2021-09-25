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
hexrom = openRomRead(filename)
for i in range(numbofbank):
     varstr = os.getcwd()
     varstr = varstr + '/' + 'maps' + '/' + str(i)
     #print(varstr)
     nmap = nbmap[i]
     mapstable = ''
     for x in range(nmap):
         varstr2 = varstr + '/' + str(x) + '.map'
         print(varstr2)
         noconnection = False
         mapfilefinal = openRomRead(varstr2)
         # Dimention map
         largeurh = readRomData(mapfilefinal, '0x0', 4).decode(encoding="utf-8")
         hauteurh = readRomData(mapfilefinal, '0x4', 4).decode(encoding="utf-8")
         largeurh = largeurh[6:8] + largeurh[4:6] + largeurh[2:4] + largeurh[0:2]
         hauteurh = hauteurh[6:8] + hauteurh[4:6] + hauteurh[2:4] + hauteurh[0:2]
         print(largeurh)
         largueurd = conv_hex2dec(largeurh)
         hauteurd = conv_hex2dec(hauteurh)
         # Tilesets
         tileset1 = readRomData(mapfilefinal, '0x8', 4).decode(encoding="utf-8")
         tileset2 = readRomData(mapfilefinal, '0xC', 4).decode(encoding="utf-8")
         tileset1 = tileset1[6:8] + tileset1[4:6] + tileset1[2:4] + tileset1[0:2]
         tileset2 = tileset2[6:8] + tileset2[4:6] + tileset2[2:4] + tileset2[0:2]
         tileset1d = conv_hex2dec(tileset1)
         tileset2d = conv_hex2dec(tileset2)
         # Dimention Bloc de bordure
         largbordh = readRomByte(mapfilefinal, '0x10').decode(encoding="utf-8")
         hautbordh = readRomByte(mapfilefinal, '0x11').decode(encoding="utf-8")
         largbordd = conv_hex2dec(largbordh)
         hautbordd = conv_hex2dec(hautbordh)
         # Bloc de bordure
         blockbord = readRomData(mapfilefinal, 31, (largbordd*hautbordd*2)).decode(encoding="utf-8")
         #Données map
         mapcoll = readRomData(mapfilefinal, 31+(largbordd*hautbordd*2), (largueurd*hauteurd*2)).decode(encoding="utf-8")
         print(mapcoll)
         # Bloc de donnnées ( musique , type de combat ...)
         block = readRomData(mapfilefinal, 28, 11).decode(encoding="utf-8")
         # Connexions
         varhex = readRomByte(mapfilefinal, conv_dec2hex((int(len(mapfilefinal)/2)-2))).decode(encoding="utf-8")
         varhex = varhex + readRomByte(mapfilefinal, conv_dec2hex((int(len(mapfilefinal)/2)-3))).decode(encoding="utf-8")
         varhex = varhex + readRomByte(mapfilefinal, conv_dec2hex((int(len(mapfilefinal)/2)-4))).decode(encoding="utf-8")
         #print(varhex)
         connection = readRomData(mapfilefinal,varhex , (int(len(mapfilefinal)/2)-4)- conv_hex2dec(varhex))
         #print(connection)
         connectiond = int((((int(len(mapfilefinal)/2)-4)- conv_hex2dec(varhex))-4)/12)
         #print(connectiond)
         nbscriptpnj = readRomByte(mapfilefinal, readRomByte(mapfilefinal, '0x1D').decode(encoding="utf-8")+readRomByte(mapfilefinal, '0x1C').decode(encoding="utf-8") ).decode(encoding="utf-8")
         nbwarp = readRomByte(mapfilefinal, add2hex((readRomByte(mapfilefinal, '0x1D').decode(encoding="utf-8")+readRomByte(mapfilefinal, '0x1C').decode(encoding="utf-8")),1)).decode(encoding="utf-8")
         nbscript = readRomByte(mapfilefinal, add2hex((readRomByte(mapfilefinal, '0x1D').decode(encoding="utf-8")+readRomByte(mapfilefinal, '0x1C').decode(encoding="utf-8")),2)).decode(encoding="utf-8")
         nbpancarte = readRomByte(mapfilefinal, add2hex((readRomByte(mapfilefinal, '0x1D').decode(encoding="utf-8")+readRomByte(mapfilefinal, '0x1C').decode(encoding="utf-8")),3)).decode(encoding="utf-8")
         scriptadr = readRomData(mapfilefinal, add2hex((readRomByte(mapfilefinal, '0x1D').decode(encoding="utf-8")+readRomByte(mapfilefinal, '0x1C').decode(encoding="utf-8")),4), 2).decode(encoding="utf-8")
         scriptadr = scriptadr[2:4] +scriptadr[0:2]
         Scriptdata = readRomData(mapfilefinal, scriptadr, (conv_hex2dec(nbscriptpnj)*24 + conv_hex2dec(nbwarp)*8 + conv_hex2dec(nbscript)*16 + conv_hex2dec(nbpancarte)*12)).decode(encoding="utf-8")
         eventdata = rea


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
