#!/usr/bin/env python3

import sys
import itertools

wordsfile = sys.argv[1]
puzzlefile = sys.argv[2]
with open(wordsfile) as f:
    validwords = set([x.strip() for x in f.readlines()])
#print(validwords)
with open(puzzlefile) as f:
    rawpuzzle = [x.strip() for x in f.readlines() if ("#" not in x) and ("[eof]" not in x)]
puzzles = [[list(c) for c in x.split("|")[0].split(",")] for x in rawpuzzle]
knownwords = [[c for c in x.split("|")[1].split(",")] for x in rawpuzzle]
for i in range(len(puzzles)):
    p = puzzles[i]
    missing = []
    allcombos = set(["".join(x) for x in list(itertools.product(*itertools.zip_longest(*p)))])
    #print(allcombos)
    for v in validwords:
        if (v in allcombos) and (v not in knownwords[i]):
            knownwords[i].append(v)
            missing.append(v)
    if missing:
        pieces = rawpuzzle[i].split("|")
        pieces[1] = pieces[1] + "," + ",".join(missing)
        print("|".join(pieces))
    else:
        print(rawpuzzle[i])
print("[eof]")
