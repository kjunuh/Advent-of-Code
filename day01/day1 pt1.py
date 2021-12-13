with open('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append(int(line.strip()))
    #lines = f.read()

print(input)
yes = 0
for i in range(len(input)-3):
    if input[i]+input[i+1]+input[i+2] < input[i+1]+input[i+2]+input[i+3]:
        yes += 1
print(yes)
