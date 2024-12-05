from pprint import pprint
import os  
import sys  
import re  
import math  
import fileinput
from string import ascii_uppercase, ascii_lowercase  
from collections import Counter, defaultdict, deque, namedtuple  
from itertools import count, product, permutations, combinations, combinations_with_replacement  

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/example', 'r') as f:
# with open(f'{dir_path}/input', 'r') as f:
    inp = f.readlines() # input is list of string lines1    
inp = [x.strip() for x in inp]
total = 0
path = []
def find_xmas(i,j,letters, total, sdir):
    if letters == []:
        return total + 1
    letter = inp[i][j]
    if inp[i][j] == letters[0] or letters[0] == -1:
        path.append((i,j))
        a,b = sdir(i,j)
        if letters == ['S']:
            return total + 1
        if 0 <= a < len(inp) and 0 <= b < len(inp[0]):
            total = find_xmas(a,b,letters[1:], total, sdir)
    return total


out = 0
dirs = [
    lambda x,y:    (x+0, y+1),  # N
    lambda x,y:    (x+1, y+1),    # NE
    lambda x,y:    (x+1, y+0),    # E
    lambda x,y:    (x+1, y-1),   # SE
    lambda x,y:    (x+0, y-1),   # S
    lambda x,y:    (x-1, y-1),  # SW
    lambda x,y:    (x-1, y+0),   # W
    lambda x,y:    (x-1, y+1),   # NW
]
for i in range(len(inp)):
    for j in range(len(inp[i])):
        for dix in dirs:
            matches = find_xmas(i, j, ['X', -1, 'M', 'A', 'S'], 0, sdir=dix)
            print(f"AHHHH{i,j,dix(i,j)}\n" if matches else "", end="")
            out += matches

print(out)
# print(path)
