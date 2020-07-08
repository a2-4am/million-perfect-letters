#!/usr/bin/env python3

import sys
import itertools

stopwordsfile = sys.argv[1]
puzzlefile = sys.argv[2]
with open(stopwordsfile) as f:
    stopwords = f.read().strip().split("|", 1).pop().split(",")
#print(stopwords)
with open(puzzlefile) as f:
    puzzles = [[list(c) for c in x.strip().split("|")[0].split(",")] for x in f.readlines() if ("#" not in x) and ("[eof]" not in x)]
for p in puzzles:
    allwords = set(["".join(x) for x in list(itertools.product(*itertools.zip_longest(*p)))])
    for s in stopwords:
        if s in allwords:
            print(s, p)
        else:
            for w in allwords:
                if s in w:
                    print(s, ["".join(x) for x in p])
                    break
