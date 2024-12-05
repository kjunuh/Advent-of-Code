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
# with open(f'{dir_path}/example', 'r') as f:
    inp = f.read()
# print(inp)
ASDF = inp.split("\n\n")
rules = ASDF[0].split('\n')
rule_list, bad_lines = [], []
for line in rules:
    rule_list.append(line.split('|'))
# print(rule_list,bad_lines)
# print(ASDF[1])
for line in ASDF[1].split('\n'):
    seen_pages = set()
    valid = True
    for page in line.split(','):
        seen_pages.add(page)
        for rule in rule_list:
            if page == rule[1]:
                if rule[0] not in seen_pages and rule[0] in line:
                    # print(rule, page, seen_pages)
                    valid = False
    if not valid:
        bad_lines.append(line)
fixed_lines = []
# for bl in bad_lines:
#     pages = bl.split(",")
#     fixed_line = []
#     for page in pages:
#         if page in fixed_line:
#             continue
#         for rule in rules:
#             if page in fixed_line:
#                 continue
#             rule = rule.split('|')
#             print(page, rule)
#             if rule[1] == page and rule[0] in pages:
#                 if page not in fixed_line:
#                     if rule[0] not in fixed_line:
#                         fixed_line += [page, rule[0]]
#                     else:
#                         fixed_line = fixed_line.index(rule[0])
        # print(fixed_line)
    # fixed_lines.append(fixed_line)
rule_dict = {}
for x, y in rule_list:
    rule_dict[y] = rule_dict.get(y, []) + [x]
print(rule_dict)
aaslekrdj = []
for bl in bad_lines:
    fixed_line = []
    for char in bl.split(","):
        i = 0
        while i < len(fixed_line):
            print(any(x in fixed_line for x in rule_dict.get(char, [])), fixed_line, rule_dict.get(char), char)
            if any(x in fixed_line[i:] for x in rule_dict.get(char, [])):
                i += 1
            else:
                break
        fixed_line = fixed_line[:i]+ [char] + fixed_line[i:]
    aaslekrdj.append(fixed_line)



pprint(aaslekrdj)
sums = 0
for gl in aaslekrdj:
    print(len(gl)//2, gl, int(gl[len(gl)//2]))
    sums += int(gl[len(gl)//2])

print(sums)
