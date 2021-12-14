with open('test.txt', 'r') as f:
    # input = ""
    # input = f.read()
    input = [line.strip("\n") for line in f]


rules = input[2:]
input = (input[:1])

for i in range(len(rules)):
    rules[i] = rules[i].split(" -> ")

# print(rules)
for elem in input:
    mStr = [char for char in elem]
# print(mStr, rules)
rDct = {}
for elem in rules:
    rDct[elem[0]] = elem[1]


# def step(target, rules):
#     for i in range(len(target)-1):
#         for rule in rules:
#             # print(target[i]+target[i+1],rule[0],target[i]+target[i+1]==rule[0], i, rule[1])
#             if target[i]+target[i+1] == rule[0]:
#                 target.insert(i,rule[1])
#     return target

def step(target, ruleDct):
    for i in range(len(target)-1):
        ops = []
        try: 
            ops.append([i,ruleDct[target[i]+target[i+1]]])
        except: 
            print(target[i]+target[i+1],'not found')
            pass
        # print(target, i, target[i]+target[i+1])
    print(ops)
    for elem in ops:
        target.insert(elem[0],elem[1])
    return target
# print(rDct['NN'])
print(step(mStr, rDct))