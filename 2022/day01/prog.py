with open("input.txt", "r") as f:
    lines = f.read()
ttots = []
for i in [map(int, x.split("\n")) for x in lines.split("\n\n")]:
    mtot = 0
    for j in i:
        mtot += j
    ttots.append(mtot)
print(sorted(ttots))
# manually summed top 3
