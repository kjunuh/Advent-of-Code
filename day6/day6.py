with open('input.txt', 'r') as f:
    input = f.read()

input = input.split(",")

input = [int(x) for x in input]

# print(input)
def Day():
    add = 0
    for ind in range(len(input)):
        if input[ind] == 0:
            input[ind] = 6
            add += 1
        else:
            input[ind] -= 1
    addList = [8]*add
    for x in addList:
        input.append(x)
    return(input)
lenx = 0

for n in range(256):
    lenx = len(Day())
    print(n+1,lenx)
