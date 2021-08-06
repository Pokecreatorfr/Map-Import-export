from romh import *
from binascii import unhexlify

def readpointer(rom, adress):
    functionhexvar = readRomData(rom, adress, 4)
    if functionhexvar[6:8] != '09' and functionhexvar[6:8] != '08':
        itsapointer = False
    if functionhexvar[6:8] == '09':
        functionhexvar = functionhexvar[0:6] + '01'
    if functionhexvar[6:8] == '08':
        functionhexvar = functionhexvar[0:6] + '0.'
    functionhexvar = functionhexvar[4:6] + functionhexvar[2:4] + functionhexvar[0:2]
    functionhexvar = functionhexvar.decode(encoding="utf-8")

    return functionhexvar

def add2hex(hex, numb):
    functionvar = conv_hex2dec(hex) + numb
    functionhexvar = conv_dec2hex(functionvar)
    return functionhexvar

def makepointer(adress):
    if len(adress) == 8:
        functionhexvar = '09' + adress[2:8]
    if len(adress) == 7:
        functionhexvar = '09' + adress[1:7]
    if len(adress) == 6:
        functionhexvar = '08' + adress[0:6]
    if len(adress) == 5:
        functionhexvar = '08' + '0' + adress[0:5]
    if len(adress) == 4:
        functionhexvar = '08' + '00' + adress[0:4]
    if len(adress) == 3:
        functionhexvar = '08' + '000' + adress[0:3]
    if len(adress) == 2:
        functionhexvar = '08' + '0000' + adress[0:2]
    if len(adress) == 1:
        functionhexvar = '08' + '00000' + adress[0:1]
    functionhexvar = functionhexvar[6:8] + functionhexvar[4:6] + functionhexvar[2:4] + functionhexvar[0:2]
    return functionhexvar

def writedatainrom(rom, data, adress):
    #print(adress)
    fonctionhexvar2 = openRomRead(rom).decode(encoding="utf-8")
    fonctionhexvar2 = unhexlify(fonctionhexvar2)
    fonctionhexvar = open(rom,'wb')
    fonctionhexvar = fonctionhexvar
    fonctionhexvar3 = unhexlify(data)
    fonctiondecvar = conv_hex2dec(adress)
    fonctionhexvar.write(fonctionhexvar2[0:fonctiondecvar] + fonctionhexvar3 + fonctionhexvar2[fonctiondecvar+len(fonctionhexvar3):len(fonctionhexvar2)])
    fonctionhexvar.close()

def searchdatainrom(rom, data):
    fonctionhexvar = conv_dec2hex(rom.find(data))
    if fonctionhexvar == 'x1':
        fonctionhexvar = '00'
    if fonctionhexvar != '00':
        if conv_hex2dec(fonctionhexvar) % 2 != 0:
            while conv_hex2dec(fonctionhexvar) % 2 != 0:
                fonctiondecvar = conv_hex2dec(fonctionhexvar) + 1
                fonctionhexvar = conv_dec2hex((rom[fonctiondecvar:]).find(data) + fonctiondecvar)
    fonctionhexvar = conv_dec2hex(int(conv_hex2dec(fonctionhexvar)/2))
    return fonctionhexvar

def freebyte(need):
    return b'ff'*need