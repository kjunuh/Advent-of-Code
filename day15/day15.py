with open('input.txt', 'r') as f:
    # input = ""
    # input = f.read()
    input = [line.strip("\n") for line in f]

field = []
for line in input:
    field.append([int(x) for x in line])

# print([x for x in field])
# print((len(input[0])-1))

dVals = []
def getPaths(field, danger,x,y):
    global dVals
    # x,y = 0,0
    danger += field[x][y]
    if (x,y) == (len(input[0])-1, len(input)-1):
        dVals.append(danger)
        # print("yes",x,y)
        return 1
    else:
        # print(x,y)
        if x+1 < len(input[0]): getPaths(field,danger,x+1,y)
        if y+1 < len(input): getPaths(field,danger,x,y+1)


getPaths(field, -field[0][0], 0,0)
print(min(dVals))
