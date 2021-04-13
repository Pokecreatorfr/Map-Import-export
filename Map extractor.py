import romh
filename = "BB.bin"
f = open(filename, "rb")
romh.readRomByte(0x000010, 0x000012)
