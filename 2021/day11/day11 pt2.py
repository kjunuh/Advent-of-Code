with open('input.txt', 'r') as f:
    # input = ""
    input = [line.strip("\n") for line in f]

mat = []
for elem in input:
    mat.append( [int(x) for x in elem])
# print(mat)

def addSurr(i,j):
    for y in [i-1,i,i+1]:
        for x in [j-1,j,j+1]:
            if not (i==y and j==x) and 0<=y<len(input) and 0<=x<len(input[0]):
                try: mat[y][x] += 1
                except: pass


def step():
    fLst = []
    oPops = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] += 1
            if mat[i][j] > 9:
                mat[i][j] = 0
                fLst.append([i,j])
    while len(fLst) != 0:
        c,d = fLst[0]
        addSurr(c,d)
        oPops.append(fLst.pop(0))
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] > 9 and [i,j] not in fLst and [i,j] not in oPops:
                    fLst.append([i,j])
                    # print(i,j)
    for i,j in oPops:
        mat[i][j] = 0 
        # print("slslek")
    # while fLst:
    #     i,j = fLst[0]
    #     # addSurr(i,j)
    #     for i in range(len(mat)):
    #         for j in range(len(mat[i])):
    #             if mat[i][j] > 9 and [i,j] not in oPops:
    #                 fLst.append([i,j])
    #     oPops.append(fLst.pop(0))

    # (oPops)
    return len(oPops) == len(mat)*len(mat[0])

n=1
while 1:
    if step():
        print(n)
        break
    n+=1