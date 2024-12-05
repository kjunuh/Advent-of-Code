from pprint import pprint
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input', 'r') as f:
    inp = f.readlines() # input is list of string lines


out = []
for line in inp:
    title, x = line.strip().split(":")
    first, second = x.strip().split("|")
    print(first, second)
    first = set([int(x.strip()) for x in first.split(" ") if x])
    second = set([int(x.strip()) for x in second.split(" ") if x])
    print(first,second)
    power = len(first.intersection(second))
    if power > 0:
        print(power)
        out.append(2**(power-1))
print(out)
print(sum(out))

