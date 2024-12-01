from pprint import pprint
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/input', 'r') as f:
    inp = f.readlines() # input is list of string lines


out = []
a,b = [], []
for line in inp:
    x,y = line.split("   ")
    a.append(x.strip())
    b.append(y.strip())

a.sort()
b.sort()

out = []
for i in range(len(a)):
    out.append(abs(int(b[i])*int(a[i])))

print(sum(out))