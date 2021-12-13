# import numpy as np
import re 
with open('input.txt', 'r') as f:
    input = ""
    input = f.read()
    # for line in f:
        # input.append(int(line.strip()))

input = input.split('\n')



# grid = np.zeros(10,10)
# grid = np.zeros(1000,1000)
# print(grid)
maxVal = 1000
grid = [[0] * maxVal for x in range(maxVal)]
# print(a)

def write(set):
    # print(set[0].strip(' ')[2])
    # print(re.split('-> | |,', set) )
    x1, x2 = int(re.split('-> | |,', set)[0]), int(re.split('-> | |,', set)[3])
    y1, y2 = int(re.split('-> | |,', set)[1]), int(re.split('-> | |,', set)[4])
    # print(x1,y1,"\n",x2,y2)
    if x1 == x2:
        # print("yass")
        if y1<y2:
            while y1 <= y2:
                grid[x1][y1] += 1
                y1 += 1
        elif y2<y1:
            while y1 >= y2:
                # print(y1,y2)
                # print(grid)
                grid[x1][y2] += 1
                # print(grid)
                y2 += 1
    
    if y1 == y2:
        if x1<x2:
            while x1 <= x2:
                grid[x1][y1] += 1
                x1 += 1
        else:
            while x1 >= x2:
                grid[x2][y2] += 1
                x2 += 1    

for elem in input:
    write(elem)
# print(grid)
cnt = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] >= 2:
            cnt += 1
print(cnt)
