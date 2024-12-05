from pprint import pprint
import os  
import sys  
import re  
import math  
import fileinput
from string import ascii_uppercase, ascii_lowercase  
from collections import Counter, defaultdict, deque, namedtuple  
from itertools import count, product, permutations, combinations, combinations_with_replacement  

# DON"T ASSUME BRUTE FORCE WILL WORK

dir_path = os.path.dirname(os.path.realpath(__file__))
# with open(f'{dir_path}/input', 'r') as f:
with open(f'{dir_path}/test', 'r') as f:
    inp = f.read() # input is list of string lines
maps = inp.split('\n\n')
mapd = {k:[y.split(" ") for y in v.strip().split("\n")] for k,v in [x.split(":") for x in maps]}
pprint(mapd)
MAXSEED = 10000

def runmap(maparr, val):
    val = int(val)
    for line in maparr:
        dest, source, rlen = map(int,line)
        if source <= val < source + rlen:
            return dest+(val-source)
    return val
# print(create_map(mapd['seed-to-soil map']))

rawmap = list(mapd.values())
seedl = rawmap[0]

# parsedmaps = [create_map(xx) for xx in rawmap[1:]]

# print(parsedmaps)
i=0
seedl = list(map(int, seedl[0]))
print(seedl)
minval = float('inf')
while i < len(seedl)-2:
    for seed in range(seedl[i], seedl[i]+seedl[i+1]):
        curval = seed
        for xmap in rawmap[1:]:
            # pprint(xmap)
            curval = runmap(xmap, curval)
        minval = min(minval, curval)
    i += 2
# print(locs)/
print(minval)