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

bankend = False
hexrom = openRomRead(filename)
for i in range(numbofbank):
    varstr = os.getcwd()
    varstr = varstr + '/' + 'maps' + '/' + str(i)
    nmap = nbmap[i]
    for x in range(nmap):
        varstr2 = varstr + '/' + str(x) + '.map'
        mapA = mapformat(openRomRead(varstr2))
        print(varstr2)
        noconnection = False
