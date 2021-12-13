with open('test.txt', 'r') as f:
    input = []
    for line in f:
        input.append(line.strip())
        # input.append(line.strip())
    
    # input = f.read()

# zero = [0,0,0,0,0,0,0,0,0,0,0,0]
# one = [0,0,0,0,0,0,0,0,0,0,0,0]

zero = [0,0,0,0,0]
one = [0,0,0,0,0]
for x in input:
    for y in range(len(x)):
        # print(x)
        if x[y] == '0':
            zero[y] += 1
        else:
            # print(y)
            one[y] += 1
mostCommon = []

for x in range(len(zero)):
    if zero[x] > one[x]:
        # zBin += '0'
        # oBin += '1'
        mostCommon.append(0)
    elif zero[x] == one[x]:
        # zBin += '2'
        # oBin += '2'
        mostCommon.append(-1)
    else:
        # zBin += '1'
        # oBin += '0'
        mostCommon.append(1)

print(mostCommon, input)
nList = [[]]
[nList[0].append(x) for x in input]
ind = 0
while ind < len(input[0]):
    for x in range(len(input)):
        # print(input[x])
        if int(input[x][ind]) == mostCommon[ind]:
            nList[ind].append(input[x])
    if len(nList[ind]) == 1:
        break
    nList.append([])
    ind += 1
print(nList)









# print(zero,one,mostCommon)

# newList = []
# ind = 0
# while len(newList) != 1:
#     for elem in input:
#         # print(int(elem[ind]) == mostCommon[ind])
#         if int(elem[ind]) == mostCommon[ind]:
#             # print('yes')
#             newList.append(elem)
#     ind += 1
# print(newList)


# #print(zBin,oBin)
# new = []
# new2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
# [new.append(x) for x in input]
# print(new)
# # for ind in range(len(new[0])):
# ind = 0
# new2 = []
# for x in new:
#     # print(x)
#     # print('test',x, ind, zBin[ind])
#     if x[ind] == zBin[ind]:
#         new2[ind].append(x)
# print()
# print(new2)


# i=0
# while len(new) != 1 and i < len(new):
#     for y in range(len(new[i])-1):
#         print(y, i)
#         print(new[i])
#         print()
#         if zBin[y] != new[y][i]:
#             new.pop(new.index(new[y]))
#     i += 1
# print(input)
