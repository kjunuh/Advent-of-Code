from pprint import pprint

with open('input', 'r') as f:
    inp = f.readlines()

inp = [x.strip() for x in inp]

pprint(inp)

nums = []

for l in inp:
    x = ""
    for c in l:
        if c.isnumeric():
            x += (c)
    nums.append(int(x[0]+x[-1]))
print(sum(nums))