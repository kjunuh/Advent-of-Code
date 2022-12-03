with open('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append(int(line.strip()))
input.append(0)
# print(input)
input.sort()
input.append(input[len(input)-1]+3)
print(input)    
threes = 0
ones = 0
# print(len(input))
for i in range(len(input)-1):
    print(input[i+1],input[i], input[i+1] - input[i])
    if input[i+1] - input[i] == 3:
        threes += 1
    if input[i+1] - input[i] == 1:
        ones += 1
#1536 too low
print(threes*ones)