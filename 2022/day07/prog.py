#!/usr/bin/env python3
import sys
import math
from collections import deque

sys.setrecursionlimit(2000000000)
try:
    fname = sys.argv[1]
except:
    fname = "input.txt"

with open(fname, "r") as f:
    inp = f.read().strip()

lines = inp.split("\n")
blocks = inp.split("\n\n")

fs, cdir = {}, {}
i = 0

import time
from pprint import pprint


def makefs():
    files = []
    dirs = []
    cdir = ""
    for line in lines:
        if line[0] == "$":
            cmd = line.split(" ")[1]
            if cmd == "cd":
                if line.split(" ")[2] == "..":
                    cdir = "-".join(cdir.split("-")[:-1])
                else:
                    cdir = cdir + "-" + line.split(" ")[2]
                    dirs.append(cdir)
        else:
            one, two = line.split(" ")
            if one.isnumeric():
                files.append([cdir + "-" + two, int(one)])
        # print(cdir)
        # if line.split(" ")[0].isnumeric():
        #     path[cdir]
    dirSizes = {}
    for folder in dirs:
        # print()
        # print(folder + ":")
        for path, size in files:
            if folder in path:
                # print(folder, path, size)
                if folder not in dirSizes.keys():
                    dirSizes[folder] = size
                else:
                    dirSizes[folder] += size
    # (70000000 - dirSizes["-/"] - 30000000 = )
    sp = 76876531
    # 70000000
    # 76876531
    # print(dirSizes)
    # print(neededSpace)
    print(dirSizes.values())
    for val in sorted(dirSizes.values()):
        if val > 6876531:
            print(val)


makefs()

# def makefs(dirName):
#     global i
#     print(dirName)
#     i += 1
#     lines = inp.split(f"$ cd {dirName}")[1].split("$ cd")[0].strip().split("\n")
#     # print(lines)
#     files = {}
#     for line in lines:
#         if line[0] == "$":
#             cmd = line.split(" ")[1]
#             if cmd == "cd":
#                 arg = line.split(" ")[2]
#         else:
#             one, two = line.split(" ")
#             if one == "dir":
#                 files[two] = makefs(two)
#             else:
#                 files[two] = int(one)
#     time.sleep(.5)
#     pprint(files)
#     print()
#     return files


path = []
