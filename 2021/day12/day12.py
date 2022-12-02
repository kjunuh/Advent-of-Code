with open('input.txt', 'r') as f:
    # input = ""
    nums = [line.strip("\n").split(",") for line in f]


inst = nums[nums.index([""])+1:]
nums = (nums[:nums.index([""])])
xs,ys = [], []
for x,y in nums:
    xs.append(int(x))
    ys.append(int(y))

# print(xs,ys)
grid = [[0] * (max(xs)+1) for _ in range(max(ys)+1)]
for x,y in nums:
    # print(int(x),int(y))
    grid[int(y)][int(x)] = 1
# print(inst)

def foldY(yVal, grid):
    top = grid[:yVal]
    bottom = grid[yVal+1:]
    # [print(f) for f in bottom]
    for i in range(len(top)):
        for j in range(len(top[0])):
            top[i][j] += bottom[(len(bottom)-1)-i][j]
    return top
    # [print(f) for f in top]

def foldX(xVal, grid):
    left, right = [], []
    for elem in grid:
        left.append(elem[:xVal])
        right.append(elem[xVal+1:])
    # [print(f) for f in right]
    # print(len(left[0]),len(right[0]))
    for i in range(len(left)):
        for j in range(len(left[0])):
            left[i][j] += right[i][(len(right[0])-1)-j]
    return left
# grid1 = foldY(7, grid)
grid2 = foldX(655,grid)
cnt = 0
# [print(f) for f in grid2]
for elem in grid2:
    for num in elem:
        if num>0: cnt += 1
print(cnt)
# [print(f) for f in grid]
