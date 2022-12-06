#!/usr/bin/env python3
import sys
from collections import deque

try:
    fname = sys.argv[1]
except:
    fname = "input.txt"

with open(fname, "r") as f:
    lines = f.read()

init, instr = lines.split("\n\n")

stacks = [deque() for i in range(1, 100)]
# print([x.split(" ") for x in init.split("\n")])
for line in init.split("\n"):
    for i in range(len(line)):
        if line[i].isalpha():
            stacks[i].append(line[i])
stacks = [i for i in stacks if i]

for line in instr.split("\n"):
    ifrom, ito, inum = (
        int(line.split(" ")[3]),
        int(line.split(" ")[5]),
        int(line.split(" ")[1]),
    )
    # print(ifrom, ito, inum)
    for i in range(inum):
        stacks[ito - 1].appendleft(stacks[ifrom - 1].popleft())
for i in stacks:
    print(i[0], end="")
print()
