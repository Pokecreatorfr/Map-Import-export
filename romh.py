"""Author: cosarara97
Version: 0.2
This module was created to make the creation of ROM-Hacking tools easier.
It uses the binascii module a lot, and some of it functions are only
used of synonyms of binascii ones."""

#import sys, os
import binascii


def conv_file2h(romFile):
    hexString = binascii.hexlify(romFile)
    return hexString


def conv_a2h(asciistr):
    """Converts ASCII hex string to it's hex equivalents."""
    hexstr = binascii.a2b_hex(asciistr)
    return hexstr


def convn_h2a(hexstr):
    """Converts hex string to it's ASCII equivalents."""
    asciistr = binascii.b2a_hex(hexstr)
    return asciistr


def conv_dec2hex(decnum):
    """Converts decimal int to it's hex equivalent
       without 0x (returns string)."""
    hexnum = hex(decnum)[2:]
    return hexnum


def conv_hex2dec(hexnum):
    """Converts hex number (string var) to it's decimal equivalent."""
    decnum = int(str(hexnum), 16)
    return decnum


def search(rom, length, start, byte="ff"):
    """Search for a certain number of repeated bytes in a string variable
       containing a ROM image in Hex. Normally used to search for FF
       bytes, which are free space in GBA ROMs, but also 00, which are free
       space in GB ROMs (i think).
       It returns the offset where all those bytes are in.
       "rom" is a string, "length" is an int, "start" is an int and "byte" is a
       string"""
    whatToSearchFor = byte * length  # whatToSearchFor = byte to search for
    # (usually ff) * length of bytes to search.
    offset_found = rom.find(whatToSearchFor, start) / 2
    return offset_found


def openRomRead(fileName):
    romOpenInReadMode = open(fileName, "rb")
    romContents = romOpenInReadMode.read()
    romOpenInReadMode.close()
    romHexString = conv_file2h(romContents)
    return romHexString


def openRomWrite(fileName):
    romOpenInWriteMode = open(fileName, 'wb')
    return romOpenInWriteMode


def readRomByte(hexRom, hexOffset):
    if hexOffset[0:2] == "0x":
        hexOffset = hexOffset[2:]
    decOffset = conv_hex2dec(hexOffset)
    byte = hexRom[decOffset * 2:decOffset * 2 + 2]
    return byte


def readRomData(hexRom, hexOffset, length):
    decOffset = conv_hex2dec(hexOffset)
    data = hexRom[decOffset * 2:decOffset * 2 + length * 2]
    return data


def insertSpacesBetweenBytes(hexstring):
    """"This is a very useful one :D If you have a sting like this:
        '36373839302d41', this function will turn it into something like this:
        '36 37 38 39 30 2d 41'. It may be useless when you are working with
        the variables, but useful when you have to show the bytes to the user"""
    new = ""
    for i in range(int(len(hexstring) / 2)):
        pos = i * 2
        new += hexstring[pos:pos + 2] + " "
    return new
    