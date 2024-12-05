from pprint import pprint
import os  
import sys  
import re  
import math  
from string import ascii_uppercase, ascii_lowercase  
from collections import Counter, defaultdict, deque, namedtuple  
from itertools import count, product, permutations, combinations, combinations_with_replacement  

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input', 'r') as f:
    inp = f.readlines() # input is list of string lines
def parse_nums(line, negatives=True):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

times = parse_nums(inp[0])
distances = parse_nums(inp[1])
time = 41
distance = 244
races = []
for total_time, dist in zip(times, distances):
    print(total_time, dist)
    win_seconds = []
    for charge_time in range(total_time):
        my_dist = ( total_time - charge_time ) * charge_time
        # my_dist = ( 66 - charge_time ) * charge_time
        if my_dist > dist:
            win_seconds.append(charge_time)
    print(win_seconds)
    races.append(len(win_seconds))
print(races, math.prod(races))

b = 41667266
ac = 976418849124160
