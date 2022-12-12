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

headpos = [0, 0]
tailpos = [0, 0]
poslist = set()
for inst in lines:
    direc, qty = inst.split(" ")
    # print(inst)
    for _, i in enumerate(range(int(qty))):
        # print(i)
        if math.dist(headpos, tailpos) == math.dist((0, 0), (1, 1)):
            cache = headpos.copy()
            # print("yes")
            # print(headpos, tailpos)
            doCorner = True
        if direc == "R":
            headpos[0] += 1
        if direc == "L":
            headpos[0] -= 1
        if direc == "U":
            headpos[1] += 1
        if direc == "D":
            headpos[1] -= 1
        if math.dist(headpos, tailpos) == math.dist((0, 0), (1, 2)) and doCorner:
            tailpos = cache
            doCorner = False
        if headpos[0] - tailpos[0] > 1:
            tailpos[0] += 1
            # if headpos[1] - tailpos[1] != 0:
            # tailpos[1] += int((headpos[1] - tailpos[1]) * 2)
        if headpos[0] - tailpos[0] < -1:
            tailpos[0] -= 1
            # if headpos[1] - tailpos[1] != 0:
            # tailpos[1] += int((headpos[1] - tailpos[1]) * 2)
            # if headpos[1] - tailpos[1] < 0:
            #     tailpos[1] -= 1
        # print("b4", headpos, tailpos)
        if headpos[1] - tailpos[1] > 1:
            tailpos[1] += 1
            # if headpos[0] - tailpos[0] != 0:
            # tailpos[0] += int((headpos[0] - tailpos[0]) * 2)
        if headpos[1] - tailpos[1] < -1:
            tailpos[1] -= 1
            # if headpos[0] - tailpos[0] != 0:
            # tailpos[0] += int((headpos[0] - tailpos[0]) * 2)
            # if headpos[0] - tailpos[0] < -1:
            #     tailpos[0] -= 1
        # if i == 1:  # and math.dist(headpos, tailpos) > math.dist((0, 0), (1, 1)):
        #     if direc == "R":
        #         tailpos[1] = headpos[1]
        #     if direc == "L":
        #         tailpos[1] = headpos[1]
        #     if direc == "U":
        #         tailpos[0] = headpos[0]
        #     if direc == "D":
        #         tailpos[0] = headpos[0]
        # print(headpos, tailpos)

        poslist.add(tuple(tailpos))
        # print(headpos, tailpos)
        # plt.scatter([x[0] for x in poslist], [x[1] for x in poslist], label=i)
        # plt.savefig("asf")
        # sleep(0.1)
        # print()
print(poslist, len(poslist))
