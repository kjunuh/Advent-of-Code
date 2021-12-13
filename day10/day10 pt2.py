with open('input.txt', 'r') as f:
    # input = ""
    input = [line.strip("\n") for line in f]

pairs = { ")" :"(", "}" :"{", ">" :"<", "]" :"[" }
vals = { ")": 1, "]": 2, "}": 3, ">": 4}

def getKey(inVal, dct):
    for key, value in dct.items():
         if inVal == value:
             return key

def isTrue(line):
    stack = []
    lst = [char for char in line]
    for char in lst:
        if char in "{[(<": stack.append(char)
        else:
            if stack[-1] == pairs[char]: stack.pop(-1)
            else: return 0
    return 1

def complete(line):
    stack = []
    lst = [char for char in line]
    for char in lst:
        if char in "{[(<": stack.append(char)
        else:
            if stack[-1] == pairs[char]: stack.pop(-1)
            else: pass
    outLst = [getKey(elem, pairs) for elem in stack]
    outLst.reverse()
    return outLst

def getScore(cmpl):
    score = 0
    for elem in cmpl:
        score *= 5
        score += vals[elem]
    return score


# print(getScore(complete("[({(<(())[]>[[{[]{<()<>>")))

newIn = []
for line in input:
    if isTrue(line):
        newIn.append(line)
print(newIn)

scores = []
for line in newIn:
    scores.append(getScore(complete(line)))
scores.sort()
print(scores[int((len(scores)/2))])