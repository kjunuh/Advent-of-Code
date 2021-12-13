import statistics as s
with open('input.txt', 'r') as f:
    input = f.read()

input = input.split(",")

input = [int(x) for x in input]

def tn(n):
    return sum(range(n + 1))

average = round(sum(input)/len(input))

# print(input)
fV = []
for i in range(max(input)):
    fuel = 0
    for x in input:
        fuel += tn(abs(x - i))
    fV.append(fuel)
    # print(i)
    

print(min(fV))