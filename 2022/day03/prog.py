from math import floor, ceil

with open("test.txt", "r") as f:
    lines = f.read().strip().split("\n")
    # inp = f.read()
outs = []
nums = []
for i in range(0, len(lines), 3):
    a, b, c = lines[i], lines[i + 1], lines[i + 2]
    print(a, b, c)

    for i in a:
        if i in b:
            if i in c:
                if not i.isupper():
                    nums.append(ord(i) - 96)
                else:
                    nums.append(ord(i) - 65 + 27)
                break
print(sum(nums), nums)
print(outs)
