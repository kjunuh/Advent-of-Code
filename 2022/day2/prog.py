with open('input.txt', 'r') as f:
    lines = [x.strip().split(' ') for x in f.read().strip().split('\n')]

# print(lines)
tot = 0
for i in lines:
    score = 0
    enem, me = i[0], i[1]
    if me == 'X': #rock lose
        score += 0
        if enem == 'A':
            score += 3
        if enem == 'B':
            score += 1
        if enem == 'C':
            score += 2

        
    if me == 'Y': #paper draw
        score += 3
        if enem == 'A': # rock
            score += 1
        if enem == 'B': # paper
            score += 2
        if enem == 'C': # scis
            score += 3
    if me == 'Z': #scis win
        score += 6
        if enem == 'A':
            score += 2
        if enem == 'B':
            score += 3
        if enem == 'C':
            score += 1
    print(score)
    tot += score
print(tot)