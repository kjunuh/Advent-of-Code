from pprint import pprint
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input', 'r') as f:
    inp = f.readlines() # input is list of string lines
sums = []
for l in inp:
    game, info = l.split(":")
    gameno = game.split(" ")[1]
    maxes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    mins = {}
    poss = True
    steps = info.split(";")
    for step in steps:
        ind = step.split(",")
        for a in ind:
            print(a)
            num, color = a.strip().split(" ")
            
            if int(num) > mins.get(color, 0):
                mins[color] = int(num)
    f = list(mins.values())      
    sums.append(f[0]*f[1]*f[2])

                

print(sum(sums))    