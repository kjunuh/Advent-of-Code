from pprint import pprint

with open('/home/kjunuh/Advent-of-Code/2023/day01/input', 'r') as f:
    inp = f.readlines()

inp = [x.strip() for x in inp]

pprint(inp)

nums = []

for l in inp:
    x = ""
    rep= {
        # j"zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9 }
    x = ""
    for i in range(len(l)):
        if l[i].isnumeric():
            x += (l[i])
        for k,v in rep.items(): 
            if l[i:].startswith(k):
                x += (str(v))
    nums.append(int(x[0]+x[-1]))
    print(nums[-1], l)
print(sum(nums))