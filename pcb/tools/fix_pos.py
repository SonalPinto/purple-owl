#!/usr/bin/python3

"""
The JLCPCB footprint for the Kailh hotswap sockets is centered around the socket alone.
Unlike the the Acheron MX100H footprint that I am using for the entire switch (holes and socket).
Hence, some fiddling is required to position the socket in the right place - which can be confirmed
in the JLCPCB assembly viewer.

Kailh hotswap socket part on JLCPCB: https://jlcpcb.com/partdetail/Kailh-CPG151101S11/C2803348
Acheron MX footprints: https://github.com/AcheronProject/acheron_MXH.pretty
"""

import sys

ofile = open(sys.argv[1], "r")
lines = ofile.readlines()
ofile.close()

ifile = open(sys.argv[2], "w")

for line in lines:
    newline = line
    if "SW_SPST" in line or "SW_Push" in line:
        items = line.split(",")

        # JLCPCB origin is at bottom-left with axes growing up and right.

        # rotate 180
        items[5] = "180.0"

        # move up by 150mil
        y = float(items[4]) + 2.54 + 1.27
        ytxt = "{:.4f}".format(y)
        items[4] = ytxt

        # move right by 25mil
        x = float(items[3]) + 1.27/2
        xtxt = "{:.4f}".format(x)
        items[3] = xtxt

        newline = ",".join(items)

    elif "R_Pack" in line:
        items = line.split(",")

        # Remove rotation from 0603x4 resistor array
        items[5] = "0.0"

        newline = ",".join(items)

    elif "74HC165" in line:
        items = line.split(",")

        # Rotate by 90 from what it is by default
        items[5] = "90.0"

        newline = ",".join(items)

    ifile.write(newline)

ifile.close()
