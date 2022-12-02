with open('input.txt', 'r') as f:
    # input = ""
    # input = f.read()
    input = [line.strip("\n") for line in f]


rules = input[2:]
input = (input[:1])

for i in range(len(rules)):
    rules[i] = rules[i].split(" -> ")

for elem in input:
    mStr = [char for char in elem]

rDct = {}
for elem in rules:
    rDct[elem[0]] = elem[1]

# print(rDct, mStr)

def step(keys, start):
    ops = []
    j = 0
    for i in range(len(start)-1):
        # print(start[i]+start[i+1])
        try: 
            ops.append([i+j+1,keys[start[i]+start[i+1]]])
            j += 1
        except: pass
    # print(ops)
    for elem in ops:
        start.insert(elem[0],elem[1])
        # print(start)
    return start

def getFreq(mLst):
    freq = {}
    for i in mLst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq 

# mStr1 = step(rDct,mStr)
# mStr2 = step(rDct,mStr1)
# mStr.insert(1,'c')
for i in range(40):
    mStr = step(rDct, mStr)
    print("step",i+1,"len:",len(mStr))
cnts = getFreq(mStr).values()
print(max(cnts)- min(cnts))
# print(getFreq(mStr))
# NcNbChB


