from romh import*
bankadress ["3526A8","3526AC","3526B0","3526B4","3526B8","3526BC","3526C0,","3526C4","3526C8","3526CC","3526D0","3526D4","3526D8","3526DC","3526E0","3526E4","3526E8","3526EC","3526F0","3526F4","3526F8","3526FC","352700","352704",'352708',"35270C","352710","352714","352718","35271C","352720","352724","352728","35272C","352730","352734","352738","35273C","352740","352744","352748","35274C","352750"]

def map():
    for i in range(0,43):
        readRomByte((bankadress[i]+(1*i)),3)
        bank [i] = data
