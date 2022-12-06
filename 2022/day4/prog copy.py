#!/usr/bin/env python3
import sys

try:
    fname = sys.argv[1]
except:
    fname = "input.txt"

with open(fname, "r") as f:
    lines = f.read().strip().split("\n")
inc = 0
for line in lines:
    a, b = line.split(",")
    al, bl = set(), set()
    for i in range(int(a.split("-")[0]), int(a.split("-")[1]) + 1):
        al.add(i)
    for i in range(int(b.split("-")[0]), int(b.split("-")[1]) + 1):
        bl.add(i)
    if al.issubset(bl) or bl.issubset(al):
        inc += 1
        print(al, bl)
print(inc)
# for i in range(len(lines)):
#     pass
