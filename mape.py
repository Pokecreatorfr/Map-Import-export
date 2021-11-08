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
    functionhexvar = functionhexvar[4:6] + \
        functionhexvar[2:4] + functionhexvar[0:2]
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
    functionhexvar = functionhexvar[6:8] + functionhexvar[4:6] + \
        functionhexvar[2:4] + functionhexvar[0:2]
    return functionhexvar


def writedatainrom(rom, data, adress):
    # print(adress)
    fonctionhexvar2 = openRomRead(rom).decode(encoding="utf-8")
    fonctionhexvar2 = unhexlify(fonctionhexvar2)
    fonctionhexvar = open(rom, 'wb')
    fonctionhexvar = fonctionhexvar
    fonctionhexvar3 = unhexlify(data)
    fonctiondecvar = conv_hex2dec(adress)
    fonctionhexvar.write(fonctionhexvar2[0:fonctiondecvar] + fonctionhexvar3 +
                         fonctionhexvar2[fonctiondecvar+len(fonctionhexvar3):len(fonctionhexvar2)])
    fonctionhexvar.close()


def searchdatainrom(rom, data):
    fonctionhexvar = conv_dec2hex(rom.find(data, 6291456))
    if fonctionhexvar == 'x1':
        fonctionhexvar = '00'
    if fonctionhexvar != '00':
        if conv_hex2dec(fonctionhexvar) % 2 != 0:
            while conv_hex2dec(fonctionhexvar) % 2 != 0:
                fonctiondecvar = conv_hex2dec(fonctionhexvar) + 1
                fonctionhexvar = conv_dec2hex(
                    (rom[fonctiondecvar:]).find(data) + fonctiondecvar)
    fonctionhexvar = conv_dec2hex(int(conv_hex2dec(fonctionhexvar)/2))
    return fonctionhexvar


def freebyte(need):
    return b'ff'*need


def write_in_hex_string(string, adress, data):
    fonctiondecvar = 2*conv_hex2dec(adress)
    string = string[0:fonctiondecvar] + data + \
        string[(fonctiondecvar+len(data)):]
    return(string)


class mapformat:
    # Classe qui permet de faire des attributs de classe a partir d'un fichier map
    def __init__(self, fichiermap,):
        # Dimention map
        self.largeurhex = readRomData(fichiermap, '0x0', 4).decode(encoding="utf-8")
        self.hauteurhex = readRomData(fichiermap, '0x4', 4).decode(encoding="utf-8")
        self.largueurdec = conv_hex2dec(self.largeurhex[0:2])
        self.hauteurdec = conv_hex2dec(self.hauteurhex[0:2])
        # Tilesets
        self.tileset1 = readRomData(fichiermap, '0x8', 4).decode(encoding="utf-8")
        self.tileset2 = readRomData(fichiermap, '0xC', 4).decode(encoding="utf-8")
        self.tileset1 = self.tileset1[6:8] + self.tileset1[4:6] + self.tileset1[2:4] + self.tileset1[0:2]
        self.tileset2 = self.tileset2[6:8] + self.tileset2[4:6] + self.tileset2[2:4] + self.tileset2[0:2]
        self.tileset1dec = conv_hex2dec(self.tileset1)
        self.tileset2dec = conv_hex2dec(self.tileset2)
        # Dimention Bloc de bordure
        self.largbordhex = readRomByte(fichiermap, '0x10').decode(encoding="utf-8")
        self.hautbordhex = readRomByte(fichiermap, '0x11').decode(encoding="utf-8")
        self.largborddec = conv_hex2dec(self.largbordhex)
        self.hautborddec = conv_hex2dec(self.hautbordhex)
        # Bloc de bordure
        self.blockbord = readRomData(fichiermap, '0x34', (self.largborddec*self.hautborddec*2)).decode(encoding="utf-8")
        #Données des collision et bytes de persmission 
        self.mapcoll = readRomData(fichiermap, add2hex('0x34', (self.largborddec*self.hautborddec*2)), (self.largborddec*self.hautborddec*2)).decode(encoding="utf-8")
        # Bloc de donnnées ( musique , type de combat ...)
        self.block = readRomData(fichiermap, 28, 12).decode(encoding="utf-8")
        #Connection 
        varhex = readRomByte(fichiermap, conv_dec2hex((int(len(fichiermap)/2)-2))).decode(encoding="utf-8") + readRomByte(fichiermap, conv_dec2hex((int(len(fichiermap)/2)-3))).decode(encoding="utf-8") + readRomByte(fichiermap, conv_dec2hex((int(len(fichiermap)/2)-4))).decode(encoding="utf-8")
        self.connection = readRomData(fichiermap, varhex, (int(len(fichiermap)/2)-4) - conv_hex2dec(varhex)).decode(encoding="utf-8")
        if self.connexions == '':
            self.noconnection = True
        #Scripts
        self.nbscriptpnj = readRomByte(fichiermap, readRomByte(fichiermap, '0x1D').decode(encoding="utf-8")+readRomByte(fichiermap, '0x1C').decode(encoding="utf-8")).decode(encoding="utf-8")
        self.nbwarp = readRomByte(fichiermap, add2hex((readRomByte(fichiermap, '0x1D').decode(encoding="utf-8")+readRomByte(fichiermap, '0x1C').decode(encoding="utf-8")), 1)).decode(encoding="utf-8")
        self.nbscript = readRomByte(fichiermap, add2hex((readRomByte(fichiermap, '0x1D').decode(encoding="utf-8")+readRomByte(fichiermap, '0x1C').decode(encoding="utf-8")), 2)).decode(encoding="utf-8")
        self.nbpancarte = readRomByte(fichiermap, add2hex((readRomByte(fichiermap, '0x1D').decode(encoding="utf-8")+readRomByte(fichiermap, '0x1C').decode(encoding="utf-8")), 3)).decode(encoding="utf-8")
        self.scriptadr = readRomData(fichiermap, add2hex((readRomByte(fichiermap, '0x1D').decode(encoding="utf-8")+readRomByte(fichiermap, '0x1C').decode(encoding="utf-8")), 4), 2).decode(encoding="utf-8")
        self.scriptadr = self.scriptadr[2:4] + self.scriptadr[0:2]
        self.Scriptdata = readRomData(fichiermap, self.scriptadr, (conv_hex2dec(self.nbscriptpnj)*24 + conv_hex2dec(self.nbwarp)*8 + conv_hex2dec(self.nbscript)*16 + conv_hex2dec(self.nbpancarte)*12)).decode(encoding="utf-8")
        self.scriptpnj = self.Scriptdata[0:(conv_hex2dec(self.nbscriptpnj) * 24 * 2)]
        self.warp = self.Scriptdata[(conv_hex2dec(self.nbscriptpnj) * 24 * 2): (conv_hex2dec(self.nbscriptpnj) * 24 * 2) + (conv_hex2dec(self.nbwarp) * 8 * 2)]
        self.script = self.Scriptdata[(conv_hex2dec(self.nbscriptpnj) * 24 * 2) + (conv_hex2dec(self.nbwarp) * 8 * 2): (conv_hex2dec(self.nbscriptpnj) * 24 * 2) + (conv_hex2dec(self.nbwarp) * 8 * 2) + (conv_hex2dec(self.nbscript) * 16 * 2)]
        self.pancarte = self.Scriptdata[(conv_hex2dec(self.nbscriptpnj) * 24 * 2) + (conv_hex2dec(self.nbwarp) * 8 * 2) + (conv_hex2dec(self.nbscript) * 16 * 2):]