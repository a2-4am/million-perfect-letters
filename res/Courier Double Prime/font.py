#!/usr/bin/env python3

def myhex(bitstring):
    return hex(int(bitstring, 2))[2:].rjust(2, "0").upper()

leftdata = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
rightdata = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
with open("font.txt", "r") as f:
    for c in 'ABCDEFGHJIKLMNOPQRSTUVWXYZ':
        #print(c)
        for row in range(16):
            left = f.read(7)
            right = f.read(7)
            f.readline()
            left = "0b1" + left[::-1]
            right = "0b1" + right[::-1]
            #print(myhex(left), myhex(right))
            leftdata[row].append(myhex(left))
            rightdata[row].append(myhex(right))
print("; This file is automatically generated")
for row in range(16):
    print("LeftFontRow%s" % row)
    for c, i in zip(leftdata[row], range(len(leftdata[row]))):
        print("         !byte $%s        ; %s" % (c, chr(i+65)))
for row in range(16):
    print("RightFontRow%s" % row)
    for c, i in zip(rightdata[row], range(len(rightdata[row]))):
        print("         !byte $%s        ; %s" % (c, chr(i+65)))