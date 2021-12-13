with open('input2.txt', 'r') as f:
    input = f.read()

input = input.split("\n")
disp, keys = [],[]
for x in input:
    disp.append(x.split("|")[1].strip(" ").split(" "))
    keys.append(x.split("|")[0].strip(" ").split(" "))

def getKey(dct, val):
    for key, value in dct.items():
        if value==val:
            return key

def inters(check, checkagainst):
    cnt = 0
    for elem in check:
        if elem in checkagainst:
            cnt += 1
    return cnt
# print("yes",inters("abcd", "adefg"))
# print(keys)

def decode(key):
    
    dct = {}
    undone = []
    for elem in key:
        elem = sorted(elem)
        elem = ''.join(elem)
        # print(elem)
        if len(elem) == 2: dct[elem] = 1
        elif len(elem) == 3: dct[elem] = 7
        elif len(elem) == 4: dct[elem] = 4
        elif len(elem) == 7: dct[elem] = 8
        if elem not in dct:
            undone.append(elem)
    for elem in undone:
        if len(elem) == 5: #5, 2, 3
            # print(getKey(dct, 1))
            if inters(elem, getKey(dct, 1))==2: dct[elem] = 3
            elif inters(elem, getKey(dct, 4)) == 3: dct[elem] = 5
            else: dct[elem] = 2
        elif len(elem) == 6: #9, 6, 0
            # print("sev", getKey(dct, 7), dct)
            if inters(elem, getKey(dct, 7)) == 3: 
                if inters(elem, getKey(dct, 4)) == 4: dct[elem] = 9
                else: dct[elem] = 0
            else: dct[elem] = 6
    return dct
            

    # print(dct)

# inc = 0
# num = ""
sum = 0
for ind in range(len(disp)):
    # print(keys[ind])
    decoded = decode(keys[ind])
    num = ""
    for value in disp[ind]:
        value = sorted(value)
        value = ''.join(value)
        num += str(decoded[value])
    sum += int(num)
print(sum)
