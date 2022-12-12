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
    pass
