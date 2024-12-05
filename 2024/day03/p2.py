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
with open(f'{dir_path}/input', 'r') as f:
    inp = f.read() # input is list of string lines

out = []


i = 0
good_str = ""
last = 0
while i < len(inp):
    print(i, good_str)
    dontind = inp[i:].find('don\'t()')
    if dontind != -1:
        good_str += inp[i:i+dontind]
        do_ind = inp[i+dontind:].find("do()")
        print("do",do_ind)
        if do_ind != -1:
            print(dontind, do_ind, i)
            i = dontind + do_ind + i            
            print(inp[i:])
        else:
            break
    else:
        good_str += inp[i:len(inp)]
        break
print(good_str)

x = (re.findall(r'mul\(-?\d+,-?\d+\)',good_str))
def parse_nums(line, negatives=True):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]
sums = 0
for a in x:
    nums = parse_nums(a)
    sums += nums[0]*nums[1]

print(sums)
