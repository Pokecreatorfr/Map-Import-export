from romh import *

def readpointer(rom, adress):
    functionhexvar = readRomData(rom, adress, 4)
    functionhexvar = functionhexvar[4:6] + functionhexvar[2:4] + functionhexvar[0:2]
    if functionhexvar[6:8] == '09':
        functionhexvar = '01' + functionhexvar
    functionhexvar = functionhexvar.decode(encoding="utf-8")
    return functionhexvar

def add2hex(hex, numb):
    functionvar = conv_hex2dec(hex) + numb
    functionhexvar = conv_dec2hex(functionvar)
    return functionhexvar
