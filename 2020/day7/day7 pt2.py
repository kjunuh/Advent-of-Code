with open('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append(line.strip())

yes = {}
for line in input:
    bag = line.split(" ")[0]+line.split(" ")[1]
    contents = []
    contents = line.split('contain')[1:]
    fcts = []
    for elem in contents:
        for x in elem.strip(" ").strip(".").split(","):
            fcts.append(x.strip(" ").split(" ")[1]+x.strip(" ").split(" ")[2])
    yes[bag] = fcts
#print(yes)

def contGold(bagColor):
    hasGold = 0
    if yes[bagColor] == ['otherbags']:
        return False
    for x in yes[bagColor]:
        if x == 'shinygold':
            return True
        else:
            if contGold(x):
                hasGold = 1
    if hasGold:
        return True

cnt = 0
for elem in yes:
    if contGold(elem):
        # print("yes",elem)
        cnt += 1
print(cnt)


# print(yes)
# print("this is a test".split(" "))