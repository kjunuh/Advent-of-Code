# from pprint import pprint
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input', 'r') as f:
    inp = f.readlines() # input is list of string lines


out = []
num_match = []
for line in inp:
    title, x = line.strip().split(":")
    first, second = x.strip().split("|")
    # print(first, second)
    first = set([int(x.strip()) for x in first.split(" ") if x])
    second = set([int(x.strip()) for x in second.split(" ") if x])
    # print(first,second)
    power = len(first.intersection(second))
    num_match.append(power)
total = 0


def aaa(arr, num):
    global total
    for i in range(num+1, num+arr[num]+1):
        total += 1
        # print(i, arr[i], end="|")
        aaa(arr, i)
    # print()
for i in range(len(num_match)):
    total += 1
    aaa(num_match, i)
# print(num_match)
print(total)
print(out)
print(sum(out))

