#!/usr/bin/env python3
import sys
import math
from collections import deque, defaultdict
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

sys.setrecursionlimit(2000000000)
try:
    fname = sys.argv[1]
except:
    fname = "input.txt"

with open(fname, "r") as f:
    inp = f.read().strip()

lines = inp.split("\n")
blocks = inp.split("\n\n")
print(lines)

cycle = 1
reg = 1
things = set()
strengths = []
for i in range(len(lines)):
    inst = lines[i].split(" ")[0]
    if inst == "addx":
        cycle += 1
        val = int(lines[i].split(" ")[1])
        reg += val
    if inst == "noop":
        pass
    if (cycle - 20) % 40 == 0 and not added:
        if cycle == 220:
            strengths.append(cycle * (reg - 1))
        else:
            strengths.append(cycle * reg)
        # strengths.append(cycle * reg)
        things.add((cycle, cycle * reg))
        print("first")
        print(cycle, reg)
        print(cycle * reg)
        print()
        cycle += 1
        added = True
    else:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            if cycle == 220:
                strengths.append(cycle * (reg - 1))
            else:
                strengths.append(cycle * reg)
            things.add((cycle, cycle * reg))
            print(cycle, reg)
            print(cycle * reg)
            print()
            added = True
        else:
            added = False
    things.add((cycle, cycle * reg))

ns = []
for cycle, st in things:
    if (cycle - 20) % 40 == 0:
        ns.append(cycle * reg)
# print(things)
print(ns, sum(ns))
print()
print(strengths)
print(sum(strengths))
