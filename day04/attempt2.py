import numpy as np
with open('input.txt', 'r') as f:
    input = f.read()

input = input.split("\n\n")

called = input[:1][0].split(",")
# print(called)
grids = input[1:]
nGrids = len(grids)

# print(grids)
# print("lsekjrlsek")
i = 0
inGrids = []
for elem in grids:
    inGrids.append(grids[i].split("\n"))
    i += 1

# print(inGrids)

for i in range(len(inGrids)):
    for j in range(len(inGrids[i])):
        inGrids[i][j] = inGrids[i][j].split()

# print(inGrids)
for i in range(len(inGrids)):
    for j in range(len(inGrids[i])):
        for k in range(len(inGrids[i][j])):
            inGrids[i][j][k] = int(inGrids[i][j][k])



def marker(chkNum, matrix):
    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            # print(matrix[row][num], chkNum, int(matrix[row][num])==int(chkNum))
            if int(matrix[row][num]) == int(chkNum):
                matrix[row][num] = -1
                # print('yes')

def isMatch(matrix):
    for row in matrix:
        total = 0
        for num in row:
            total += num
        if total == -5:
            return True
    return False

def rotate(myList):
    return list(zip(*reversed(myList)))
myList = inGrids[0]

# print(inGrids)
def run(): 
    for calledNum in called:

        for listIndex in range(len(inGrids)):
            marker(calledNum, inGrids[listIndex])
            if isMatch(rotate(inGrids[listIndex])) or isMatch(inGrids[listIndex]):
                return inGrids[listIndex], calledNum
        # print(calledNum)
        # print(inGrids)
# for calledNum in called:
#     print(calledNum)
#     marker(calledNum, inGrids[0])
#     print(inGrids[0])
finalGrid = run()
sum = 0
for elem in finalGrid[0]:
    for num in elem:
        if num != -1:
            sum += num
            
print(sum*int(finalGrid[1]))











# print(myList)
# marker(22, inGrids[0])
# print(inGrids[0])
# print(rotate(inGrids[0]))
# print(isMatch(rotate(inGrids[0])))
# print(grids)
# for i in range(len(grids)):
#     for j in range(len(grids)):
#         grids[i][j] = grids[i][j].split()

# for x in grids:
#     print(x)
# print("new\n")
# print(grids)