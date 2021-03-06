#!/usr/bin/env python3

def myhex(bitstring):
    return hex(int(bitstring, 2))[2:].rjust(2, "0").upper()

data = [ [], [], [], [], [], [], [], [] ]
with open("font.txt", "r") as f:
    for c in map(chr, range(33, 91)):
        f.readline()
        for row in range(8):
            rawbits = f.readline().strip()
            bits = "0b1" + rawbits[::-1]
            data[row].append(myhex(bits))
print("; Heavy Silk pixel font")
print("; (c) 2020 by 4am")
print("; license:Open Font License 1.1, see OFL.txt")
print("; This file is automatically generated")
for row in range(8):
    print("HeavySilkRow%s" % row)
    print("         !byte $80        ; space")
    for c, i in zip(data[row], range(len(data[row]))):
        print("         !byte $%s        ; %s" % (c, chr(i+33)))
