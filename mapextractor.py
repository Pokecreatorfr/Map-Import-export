from romh import *
from mape import *
from Value import *
filename = "BPRE0.gba"



hexrom = openRomRead(filename)
for i in range(43):
    bankp[i] = readRomData(hexrom, listadre[i], 3)
for x in range(43):
    hexv = bankp[x]
    bankp[x] = hexv[4:6] + hexv [2:4] + hexv[0:2]
    bankp[x] = bankp[x].decode(encoding="utf-8")
    nmap = nbmap[x]
    for i in range(nmap):
        mapp[i] = conv_hex2dec(bankp[x])+4*i
        mapp[i] = conv_dec2hex(mapp[i])
        hexv = mapp[i]
        #read block
        varadr = readRomData(hexrom, hexv, 3)
        varadr = varadr[4:6] + varadr [2:4] + varadr[0:2]
        varadr = varadr.decode(encoding="utf-8")
        vardec = conv_hex2dec(varadr) + 16
        varadr = conv_dec2hex(vardec)
        block = readRomData(hexrom, varadr, 12)
        #read largeurh and hauteurh
        varadr = readRomData(hexrom, hexv, 3)
        varadr = varadr[4:6] + varadr [2:4] + varadr[0:2]
        varadr = varadr.decode(encoding="utf-8")
        varadr = readRomData(hexrom, varadr, 3)
        varadr = varadr.decode(encoding="utf-8")
        varadr = varadr[4:6] + varadr [2:4] + varadr[0:2]
        largeurh = readRomData(hexrom, varadr, 4)
        vardec = conv_hex2dec(varadr) + 4
        varadr = conv_dec2hex(vardec)
        hauteurh = readRomData(hexrom, varadr, 4)
        largeurh = largeurh.decode(encoding="utf-8")
        hauteurh = hauteurh.decode(encoding="utf-8")
        largueurd = conv_hex2dec(largeurh[0:2])
        hauteurd = conv_hex2dec(hauteurh[0:2])
        mapcollseize = largueurd * hauteurd * 2
        vardec = conv_hex2dec(varadr) + 8
        varadr = conv_dec2hex(vardec)
        varadr = readRomData(hexrom, varadr, 3)
        varadr = varadr[4:6] + varadr [2:4] + varadr[0:2]
        varadr = varadr.decode(encoding="utf-8")
        mapcoll = readRomData(hexrom, varadr, mapcollseize)
        print(mapcoll)
    print(mapp)
    print(bankp)
#print(bankp)
#print(mapp)
