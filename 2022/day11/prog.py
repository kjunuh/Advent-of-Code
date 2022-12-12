#!/usr/bin/env python3
import sys
import math
from collections import deque, defaultdict
import numpy as np
from pprint import pprint

try:
    fname = sys.argv[1]
except:
    fname = "input.txt"

with open(fname, "r") as f:
    inp = f.read().strip()

lines = inp.split("\n")
grid = [list(map(ord, y)) for y in [list(x) for x in lines]]

for i in range(len(grid)):
    grid[i] = [x - ord("a") for x in grid[i]]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == -14:
            start = [i, j]
            grid[i][j] = 0
        if grid[i][j] == -28:
            end = [i, j]
            grid[i][j] = ord("z") - ord("a")

pos = start
visited = []
moves = []
while pos != end:

    # print(grid[pos[0] + 1][pos[1]] - grid[pos[0]][pos[1]])
    try:
        if [[i + 1][j]] in visited:
            print("t")
            continue
        print("yes")
        print(grid[pos[0] + 1][pos[1]] - grid[pos[0]][pos[1]])
        if grid[pos[0] + 1][pos[1]] - grid[pos[0]][pos[1]] <= 1:
            print("aseklrj")
            moves.append([i + 1, j])
    except:
        pass

    try:
        if [[i - 1][j]] in visited:
            print("t")
            continue
        if grid[i - 1][j] - grid[pos[0]][pos[1]] <= 1:
            moves.append([i + 1, j])
    except:
        pass

    try:
        if [[i][j + 1]] in visited:
            print("t")
            continue
        if grid[i][j + 1] - grid[pos[0]][pos[1]] <= 1:
            moves.append([i + 1, j])
    except:
        pass

    try:
        if [[i][j - 1]] in visited:
            print("t")
            continue
        if grid[i][j - 1] - grid[pos[0]][pos[1]] <= 1:
            moves.append([i + 1, j])
    except:
        pass
    visited.append(pos)
    print(moves)
    break
pprint(grid)
