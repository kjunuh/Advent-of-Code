with open('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append(line.strip())
        # input.append(line.strip())
yes = []
for x in input:
    yes.append(x.split(" "))

print(yes)

horiz = 0
vert = 0
aim = 0
for x in yes:
    if x[0] == 'forward':
        horiz += int(x[1])
        vert += int(x[1])*aim

    if x[0] == 'down':
        aim += int(x[1])
        # vert += int(x[1])*aim
    if x[0] == 'up':
        aim -= int(x[1])
        # vert -= int(x[1])*aim

print(horiz*vert)