from pprint import pprint
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input', 'r') as f:
    inp = f.readlines() # input is list of string lines


def hassym(i, j, arr=inp):
    coords = [
    (i+1,j),
    (i-1,j),
    (i,j+1),
    (i,j-1),

    # corners
    (i+1,j+1),
    (i+1,j-1),
    (i-1,j+1),
    (i-1,j-1)] 
    
    surrounding = []
    for x,y in coords:
        try:
            surrounding.append(arr[x][y])
        except IndexError:
            surrounding.append(".")
    print(arr[i][j], surrounding)
    out = []
    for num, v in enumerate(surrounding):
        if v == "*":
            print("found", v, coords[num], num)
            out += [coords[num]]
    # if any([x in surrounding for x in "!@#$%^&*()-=+/"]):
        # return True
    return out or False

nums = []
geardict = {}
for i,line in enumerate(inp):
    j = 0
    while j < len(line):
        valid = False
        gearcoords = False
        num = ""
        while line[j].isnumeric():
            gearcoords = gearcoords or hassym(i,j)
            num += (line[j])
            j += 1
        if gearcoords:
            for gearcoord in gearcoords:
                print(geardict, num, int(num))
                geardict[gearcoord] = geardict.get(gearcoord, []) + [int(num)]
                print('after', geardict, int(num))
        # if valid:
        #     print(num, valid)
        #     nums.append(int(num))
        elif num:
            print(num)
        j += 1
print(geardict)
for k,v in geardict.items():
    if len(v) == 2:
        nums.append(int(v[0])*int(v[1]))
print(sum(nums))
        