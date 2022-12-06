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
        if len(buf) > 14:
            buf.popleft()
        print(buf)
        if len(set(buf)) == 14:
            return i + 1


print(getx(inp))
# so close. wasted time turning it into a function instead of using break (idk why), maybe could have leaderboarded today but prob not.
