from romh import *
from mape import *
from Value import *
filename = "BPRE0.gba"



hexrom = openRomRead(filename)
for i in range(43):
    bankp[i] = readRomData(hexrom, listadre[i], 3)
    depointl(bankp,i)
    bankp[i] = conv_hex2dec(bankp[i])
print(bankp)
