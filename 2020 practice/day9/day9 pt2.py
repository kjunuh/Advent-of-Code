targetSum = 248131121
with open('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append(int(line.strip()))

def test(index):
    sum = 0
    while sum <= targetSum:
        sum += input[index]
        if sum == targetSum:
            return index
        index += 1
    return False

for i in range(len(input)):
    if test(i):
        print(input[i:test(i)])