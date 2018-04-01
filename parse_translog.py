#!/usr/bin/env python

import os, sys, re

# Set blocksize
blocksize = 1024

# Read arguments
filename = sys.argv[1]


def read_file(filename):

    with open(filename,"rb") as f:
        block = f.read(blocksize)
	str = ""
	for ch in block:
            str +=  "%02x" % ord(ch)
    return  str

def parse_updates(hexdata,asciidata):

    updates = ""    
    pattern = re.compile(r'080[0-9](\w+?)045f646f63\w+?(7b\w+?7d)')

    for entry in re.findall(pattern, hexdata):
        updates += "Document ID: %s\n%s\n" % (entry[0].decode("hex"),entry[1].decode("hex"))

    return updates


hexdata = read_file(filename)
print parse_updates(hexdata,hexdata.decode("hex"))
