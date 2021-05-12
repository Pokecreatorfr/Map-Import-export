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
    varhex2 = varhex[34:36] + varhex[32:34]
    vardec = conv_hex2dec(varhex2)
    if vardec > 500:
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
    varadr = readpointer(hexrom,varadr)
    varadr = add2hex(varadr, -4)
    itsamap = True
    numbofmap = 0
    #print(varadr)
    while itsamap == True:
        varadr = add2hex(varadr, 4)
        varhex = readRomData(hexrom, varadr, 28).decode(encoding="utf-8")
        if varhex[6:8] != '08' and varhex[6:8] != '09':
            itsamap = False
        if varhex[14:16] != '08' and  varhex[14:16] != '09' and varhex[14:16] != '00':
            itsamap = False
        if varhex[22:24] != '08' and  varhex[22:24] != '09' and varhex[22:24] != '00':
            itsamap = False
        varhex2 = varhex[34:36] + varhex[32:34]
        vardec = conv_hex2dec(varhex2)
        if vardec > 500:
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
        varhex2 = varhex[34:36] + varhex[32:34]
        numbofmap = numbofmap + 1
        if itsapointer == False :
            itsamap = False
        if itsabank == False :
            numbofmap = numbofmap - 1
        if itsabank == True :
            nbmap[numbofbank - 1] = numbofmap
        print(numbofmap)
    #print(nbmap)
