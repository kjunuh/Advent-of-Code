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
# with open(f'{dir_path}/example', 'r') as f:
with open(f'{dir_path}/input', 'r') as f:
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
# dirs = [
ne = lambda x,y:    (x+1, y+1)      # NE
sw =  lambda x,y:    (x-1, y-1)      # SW
   
    # lambda x,y:    (x+0, y+1),  # N
    # lambda x,y:    (x+1, y+0),    # E
    # lambda x,y:    (x+0, y-1),   # S
    # lambda x,y:    (x-1, y+0),   # W
nw =  lambda x,y:    (x-1, y+1)   # N
se =  lambda x,y:    (x+1, y-1)   # SE
# ]

def findx(i,j):
    one = (inp[ne(i,j)[0]][ne(i,j)[1]] == 'M' and inp[sw(i,j)[0]][sw(i,j)[1]] == "S") or (inp[ne(i,j)[0]][ne(i,j)[1]] == 'S' and inp[sw(i,j)[0]][sw(i,j)[1]] == "A")
    two = (inp[nw(i,j)[0]][nw(i,j)[1]] == 'M' and inp[se(i,j)[0]][se(i,j)[1]] == "S") or (inp[nw(i,j)[0]][nw(i,j)[1]] == 'S' and inp[se(i,j)[0]][se(i,j)[1]] == "A")
    return one and two
out = 0
for i in range(1,len(inp)-1):
    for j in range(1,len(inp[i])-1):
        if inp[i][j] == "A":
            if set((inp[i+1][j+1],inp[i-1][j-1])) == set(('M', "S")) and set((inp[i-1][j+1],inp[i+1][j-1])) == set(('M', "S")):
                print(i,j)
                out += 1

print(out)
# print(path)
