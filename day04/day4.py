import numpy as np
with open('test.txt', 'r') as f:
    input = ""
    input = f.read()
    # for line in f:
        # input.append(int(line.strip()))

input = input.split("\n\n")
# print(input)


mat = np.zeros((nGrids,5,5))
# print(input)

called = input[:1]
grids = input[1:]
# print(grids)
nGrids = len(grids)
newNums = []
# for elem in grids:
#     rows = elem.split("\n")
#     # print(rows)
#     for row in rows:
#         nums = row.split(" ")
#         for num in nums:
#             if num != '':
#                 newNums.append(num)



for i in range(len(grids)):
    grids[i] = grids[i].split("\n")

for i in range(len(grids)):
    for j in range(len(grids)):
        grids[i][j] = grids[i][j].split(" ")



print(grids)
# print(newNums)
i = 0
j = 0
# print(len(newNums))
numGrids = np.zeros((nGrids,5,5))

for i in range(int(len(newNums)/5)):
    # print(newN
    # ums[5*(i-1):5*i])
    pass


# print(numGrids)
        

# 0   0 0
# 1   0 1
# 2   0 2
# 3   0 3
# 4   0 4
# 5   1 0


