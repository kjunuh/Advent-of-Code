with open('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append(int(line.strip()))
    
def test(index):
    num = input[25+index]
    pream = input[index:index+25]
    for i in range(len(pream)):
        for j in range(len(pream)):
            if i != j:
                #print(pream[i], pream[j], pream[i]+pream[j])
                if pream[i]+pream[j] == num:
                    return True
    return False

for index in range((len(input)-25)):
    if not test(index):
        print(input[25+index])
