with open('test.txt', 'r') as f:
    # input = ""
    input = []
    for line in f:
        input.append(line.strip("\n"))

# def makeList(line):
#     dct = [[[],[]],[[],[]],[[],[]]]
#     for char in line:

#         if char == "[": dct[0][0].append("[")
#         if char == "]": dct[0][1].append("]")
    
#         if char == "(": dct[1][0].append("(")
#         if char == ")": dct[1][1].append(")")
        
#         if char == "<": dct[2][0].append("<")
#         if char == ">": dct[2][1].append(">")
#     return dct

# print(makeList(input[0]))

pairs = {
    "(" : ")",
    "{" : "}",
    "<" : ">",
    "[" : "]",
}

def removePair(elemInd, charLine):
    line = [char for char in charLine]
    # for ind in range(elemInd,len(line)):
    # print(line)
    ind = elemInd+1
    while ind < len(line):
        if line[ind] == line[elemInd]:
            line = removePair(ind,line)
        # print(ind,"1",pairs[line[elemInd]],"2", line[ind])
    
        if pairs[line[elemInd]] == line[ind]:
            # print(ind,"ind\n")
            line.pop(elemInd)
            line.pop(ind-1)
        
        ind += 1
    return line

# print(pairs["("])
yes = "[({(<(())[]>[[{[]{<()<>>"
i = 0
yesOld = "lsekjrlse"
# while i < len(yes)/2:
while i < len(yes):
    if yes[i] in ["(","<","["]:
        yes = removePair(i, yes) 
        # if yesOld == yes:
        #     print(i,yes[i],"breakkk\n")
        #     break
        yesOld = yes
    print(yes)
print(yes)
# { ( [ ( < { } [ < > [ ] } > { [ ] { [ ( < ( ) > 