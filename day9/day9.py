with open('input.txt', 'r') as f:
    # input = ""
    input = []
    for line in f:
        input.append(line.strip("\n"))

# def findMin(i,j, input):
#     num = input[i][j]
#     if i == 0 and j == 0:
#         if num < input[i+1][j] and num < input[i][j+1]:
#             return num
#     elif i == 0:
#         if num < input[i][j+1] and num < input[i][j-1] and num < input[i+1][j]:
#             return num
#     elif j == 0:
#         if num < input[i][j+1] and num < input[i+1][j] and num < input[i][j-1]:
#             return num
#     else:
#         if num < input[i+1][j] and num < input[i-1][j] and num < input[i][j-1] and num < input[i][j+1]:
#             return num
#     return -1

def getSurr(i,j,input):
    surr = []

    if 0<=i+1<len(input):
        surr.append(input[i+1][j])

    if 0<=i-1<len(input):
        surr.append(input[i-1][j])

    if 0<=j+1<len(input[i]):
        surr.append(input[i][j+1])

    if 0<=j-1<len(input[i]):
        surr.append(input[i][j-1])
 
    return surr

mins = []
for i in range(len(input)):
    for j in range(len(input[i])):
        isMin = True
        for num in getSurr(i,j,input):
            if input[i][j] >= num:
                isMin = False
        if isMin:
            # print(i,j)
            mins.append(int(input[i][j]))

add = 0
for elem in mins:
    add += elem+1
# 100x100
print(mins)
print(getSurr(99,99,input))
print(add)