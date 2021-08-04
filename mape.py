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
        functionhexvar = '09' + adress[2:4] + adress[4:6] + adress[6:8]
    if len(adress) == 7:
        functionhexvar = '09' + adress[1:3] + adress[3:5] + adress[5:7]
    if len(adress) == 6:
        functionhexvar = '08' + adress[0:2] + adress[2:4] + adress[4:6]
    if len(adress) == 5:
        functionhexvar = '08' + '0' +adress[0] + adress[1:3] + adress[3:5]
    if len(adress) == 4:
        functionhexvar = '08' + '00' + adress[0:2] + adress[2:4]
    functionhexvar = functionhexvar[6:8] + functionhexvar[4:6] + functionhexvar[2:4] + functionhexvar[0:2]
    return functionhexvar

def writedatainrom(rom, data, adress):
    print(adress)
    fonctionhexvar2 = openRomRead(rom).decode(encoding="utf-8")
    fonctionhexvar2 = unhexlify(fonctionhexvar2)
    fonctionhexvar = open(rom,'wb')
    fonctionhexvar = fonctionhexvar
    fonctionhexvar3 = unhexlify(data)
    fonctiondecvar = conv_hex2dec(adress)
    fonctionhexvar.write(fonctionhexvar2[0:fonctiondecvar] + fonctionhexvar3 + fonctionhexvar2[fonctiondecvar+len(fonctionhexvar3):len(fonctionhexvar2)])
    fonctionhexvar.close()
