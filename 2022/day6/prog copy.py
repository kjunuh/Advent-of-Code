#!/usr/bin/env python3
import sys
from collections import deque

try:
    fname = sys.argv[1]
except:
    fname = "input.txt"

with open(fname, "r") as f:
    inp = f.read()
    # lines = inp.split("\n")
buf = deque()


def getx(inp):
    for i in range(len(inp)):
        buf.append(inp[i])
        if len(buf) > 4:
            buf.popleft()
        print(buf)
        if len(set(buf)) == 4:
            return i + 1


print(getx(inp))
