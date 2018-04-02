#!/usr/bin/env python

import os, sys, re

# Set blocksize
blocksize = 1024

def read_header(filename):

    with open(filename,"rb") as f:
        block = f.read(blocksize)
        str = ""
        for ch in range (0, 6):
            str +=  "%02x" % ord(block[ch])
    return  str

def match_header(header):

    header_types = {
        '3fd76c170874' : 'TRANSLOG',
        '3fd76c170873' : 'SEGMENTS',
        '3fd76c17174c' : 'CFE',
        '3fd76c17144c' : 'CFS',
        '3fd76c17124c' : 'FNM',
        '3fd76c17134c' : 'SI',
        '3fd76c17114c' : 'NVD',
        '3fd76c17154c' : 'NVM/DVD',
        '3fd76c171c4c' : 'FDT',
        '3fd76c171d4c' : 'FDX',
        '3fd76c17184c' : 'DII/DIM',
        '3fd76c17194c' : 'DOC/POS/DVM',
        '3fd76c171342' : 'TIP',
        '3fd76c171242' : 'TIM'
    };

    if header in header_types.keys():
        return header_types[header]
    else:
        return "Unknown header"

# Read filename
filename = sys.argv[1]

# Read first 6 bytes from header   
hexdata = read_header(filename)

# Return the file type
print "Detected file type " + match_header(hexdata)
