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
        varadr = readpointer(hexrom,hexv)
        varadr = add2hex(varadr, 16)
        block = readRomData(hexrom, varadr, 12)
        #read largeurh and hauteurh
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        largeurh = readRomData(hexrom, varadr, 4)
        varadr = add2hex(varadr, 4)
        hauteurh = readRomData(hexrom, varadr, 4)
        largeurh = largeurh.decode(encoding="utf-8")
        hauteurh = hauteurh.decode(encoding="utf-8")
        largueurd = conv_hex2dec(largeurh[0:2])
        hauteurd = conv_hex2dec(hauteurh[0:2])
        mapcollseize = largueurd * hauteurd * 2
        varadr = add2hex(varadr, 8)
        varadr = readpointer(hexrom, varadr)
        mapcoll = readRomData(hexrom, varadr, mapcollseize)
        mapcoll = mapcoll.decode(encoding="utf-8")
        # Read tileset informations*
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        varadr = add2hex(varadr, 16)
        varadr2 = readpointer(hexrom, varadr)
        vardec2 = conv_hex2dec(varadr2)
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        varadr = add2hex(varadr, 20)
        varadr3 = readpointer(hexrom, varadr)
        vardec3 = conv_hex2dec(varadr3)
        tileset1d = (vardec2 - tilesetstart) / 24
        tileset2d = (vardec3 - tilesetstart) / 24
        varhex2 = conv_dec2hex(int(tileset1d))
        varhex3 = conv_dec2hex(int(tileset2d))
        if len(varhex2) == 1:
            varhex2 = "0" + varhex2
        if len(varhex3) == 1:
            varhex3 = "0" + varhex3
        tileset1 = varhex2 + "000000"
        tileset2 = varhex3 + "000000"
        #Read bodure block informations
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        varadr = add2hex(varadr, 24)
        largbordh = readRomByte(hexrom, varadr)
        largbordh = largbordh.decode(encoding="utf-8")
        largbordd = conv_hex2dec(largbordh)
        varadr = add2hex(varadr, 1)
        hautbordh = readRomByte(hexrom, varadr)
        hautbordh= hautbordh.decode(encoding="utf-8")
        hautbordd = conv_hex2dec(hautbordh)
        size = (hautbordd * largbordd) * 2
        #Read bodure block
        varadr = readpointer(hexrom, hexv)
        varadr = readpointer(hexrom, varadr)
        varadr = add2hex(varadr, 8)
        varadr = readpointer(hexrom, varadr)
        blockbord = readRomData(hexrom, varadr, size).decode(encoding="utf-8")
        #Read event
        varadr = readpointer(hexrom, hexv)
        varadr = add2hex(varadr, 4)
        varadr = readpointer(hexrom, varadr)
        pnjscripth = readRomByte(hexrom, varadr)
        varadr = add2hex(varadr, 1)
        warph = readRomByte(hexrom, varadr)
        varadr = add2hex(varadr, 1)
        scripth = readRomByte(hexrom, varadr)
        varadr = add2hex(varadr, 1)
        pancarteh = readRomByte(hexrom, varadr)
        pnjscripth = pnjscripth.decode(encoding="utf-8")
        warph = warph.decode(encoding="utf-8")
        scripth = scripth.decode(encoding="utf-8")
        pancarteh = pancarteh.decode(encoding="utf-8")
        pnjscriptd = conv_hex2dec(pnjscripth)
        warpd = conv_hex2dec(warph)
        scriptd = conv_hex2dec(scripth)
        pancarted = conv_hex2dec(pancarteh)
        varadr = add2hex(varadr, 1)
        varadr2 = readpointer(hexrom, varadr)
        size = pnjscriptd * 24
        varhex2 = readRomData(hexrom, varadr2, size)
        varhex2 = varhex2.decode(encoding="utf-8")
        mapevent = varhex2
        varadr = add2hex(varadr, 4)
        varadr2 = readpointer(hexrom, varadr)
        size = warpd * 8
        varhex2 = readRomData(hexrom, varadr2, size)
        varhex2 = varhex2.decode(encoding="utf-8")
        mapevent = mapevent + varhex2
        size= scriptd * 16
        varadr2 = add2hex(varadr, 4)
        varhex2 = readRomData(hexrom, varadr2, size)
        varhex2 = varhex2.decode(encoding="utf-8")
        mapevent = mapevent + varhex2
        size = pancarted * 12
        varadr2 = add2hex(varadr, 4)
        varhex2 = readRomData(hexrom, varadr2, size)
        varhex2 = varhex2 = varhex2.decode(encoding="utf-8")
        mapevent = mapevent + varhex2
        mapevent = mapevent + pnjscripth + warph + scripth + pancarteh
        # Read connection informations
        varadr = readpointer(hexrom, hexv)
        varadr = add2hex(varadr, 4)
        varadr = readpointer(hexrom, varadr)
        
        print(mapevent, pnjscripth, warph, scripth, pancarteh)

    #print(mapp)
    print(bankp)
#print(bankp)
#print(mapp)
