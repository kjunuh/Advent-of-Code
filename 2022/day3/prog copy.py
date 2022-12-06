from math import floor, ceil

with open("test.txt", "r") as f:
    lines = f.read().strip().split("\n")
    # inp = f.read()
outs = []
nums = []
for line in lines:
    print(int(floor(len(line) / 2)))
    a, b = line[: int(floor(len(line) / 2))], line[int(floor(len(line) / 2)) :]
    print(a, b)

    for i in a:
        if i in b:
            if not i.isupper():
                nums.append(ord(i) - 96)
            else:
                nums.append(ord(i) - 65 + 27)
            break
print(sum(nums))
# print(outs)
