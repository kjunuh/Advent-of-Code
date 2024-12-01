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
        except:
            pass
    print(arr[i][j], surrounding)
    if any([x in surrounding for x in "!@#$%^&*()-=+/"]):
        return True
    return False

nums = []
for i,line in enumerate(inp):
    j = 0
    while j < len(line):
        valid = False
        num = ""
        while line[j].isnumeric():
            valid = valid or hassym(i,j)
            num += (line[j])
            j += 1
        if valid:
            print(num, valid)
            nums.append(int(num))
        elif num:
            print(num)
        j += 1

print(sum(nums))
        