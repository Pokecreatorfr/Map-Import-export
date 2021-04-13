from romh import *
from mape import *
from Value import *
filename = "BPRE0.gba"


hexrom = openRomRead(filename)
for i in range (0,43):
    bankp[i] = readRomData(hexrom, listadre[i], 3)
    for x in range (0,43):
        depoint(bankp,x)


print(bankp)
