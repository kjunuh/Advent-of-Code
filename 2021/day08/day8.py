with open('input2.txt', 'r') as f:
    input = []
    for line in f:
        input.append(line.strip("\n")[60:])

input = [x.split() for x in input]

inc = 0
for x in input:
    if len(x) == 4:
        for y in x:
            if len(y) in [2, 3, 4, 7]:
                inc += 1
                # print(y)

print(inc)