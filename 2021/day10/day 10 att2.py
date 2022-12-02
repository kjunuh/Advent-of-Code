with open('input.txt', 'r') as f:
    # input = ""
    input = [line.strip("\n") for line in f]
pairs = { ")" :"(", "}" :"{", ">" :"<", "]" :"[" }
def testLine(line):
    stack = []
    lst = [char for char in line]
    for char in lst:
        if char in "{[(<": stack.append(char)
        else:
            if stack[-1] == pairs[char]: stack.pop(-1)
            else: return char
    return 0
vals = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    0 : 0,
}
total = 0
for line in input:
    total += vals[testLine(line)]
print(total)