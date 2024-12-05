from pprint import pprint
import os, sys, re, math

from string import ascii_uppercase, ascii_lowercase  
from collections import Counter, defaultdict, deque, namedtuple  
from itertools import count, product, permutations, combinations, combinations_with_replacement  
# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                        AB AC AD BA    BC BD CA CB    CD DA DB DC
# combinations_with_replacement('ABCD', 2)    AA AB AC AD    BB BC BD       CC CD          DD
# combinations('ABCD', 2)                        AB AC AD       BC BD          CD
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input', 'r') as f:
    inp = f.readlines() # input is list of string lines

def parse_nums(line, negatives=True):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]

## START

def issafe(arr):
    diffs = []
    ascend = False
    descend = False
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if abs(diff) > 3 or diff == 0: 
            return False
        diffs.append(diff)
    # print(diffs)
    if all(x >= 0 for x in diffs) or all(x <= 0 for x in diffs):
        return True
    return False
safe = 0
for level in inp:
    nums = parse_nums(level)
    print(nums, issafe(nums))
    if any(issafe(nums[:j]+nums[j+1:]) for j in range(len(nums))):
        safe += 1

    
# print(len(inp)-safe)
print(safe)

