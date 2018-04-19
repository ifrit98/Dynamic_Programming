from math import inf

def extraSpace(S, M, i, j):
    L = [len(word) for word in S]
    Ldim = L[i:j+1]

    a = M - j + i
    b = sum(Ldim)

    return a - b


def badnessLine(S,M,i,j):
    e = extraSpace(S,M,i,j)

    if e < 0:
        return inf
    else:
        return e


def minBad(S,M,i):
    if badnessLine(S,M,i,len(S)) != inf:
        return 0

    current = inf
    next = 0

    for k in range(len(S),i-1,-1):
        temp = badnessLine(S,M,i,k)
        if temp < current:
            current = temp
            i = k
        next = minBad(S,M,i+1)

    return current if current > next else next


def minBadDynamic(S,M):
    c = [[0 for x in S] for y in S]

    for i in range(0, len(S)):
        c[i][i] = M - len(S[i])
        for j in range(i+1, len(S)):
            c[i][j] = badnessLine(S,M,i,j)

    best_cost = [0 for x in S]

    for i in reversed(range(-1,len(S)-1)):
        best_cost[i] = c[i][len(S)-1]
        for j in reversed(range(i, len(S))):
            if c[i][j-1] == inf or (i == 0 and j == 0):
                continue
            if best_cost[i] > best_cost[j] + c[i][j-1]:
                best_cost[i] = best_cost[j] + c[i][j-1]

    return best_cost[0]


def minBadDynamicChoice(S, M):
    c = [[0 for x in S] for y in S]

    for i in range(0, len(S)):
        c[i][i] = M - len(S[i])
        for j in range(i+1, len(S)):
            c[i][j] = badnessLine(S,M,i,j)

    best_cost, choices = [0 for x in S], [0 for x in S]

    for i in reversed(range(-1,len(S)-1)):
        best_cost[i] = c[i][len(S)-1]
        choices[i] = len(S)
        for j in reversed(range(i, len(S))):
            if c[i][j-1] == inf:
                continue
            if best_cost[i] > best_cost[j] + c[i][j-1]:
                best_cost[i] = best_cost[j] + c[i][j-1]
                choices[i] = j

    print('Best cost:',best_cost[0])

    return best_cost, choices


def printParagraph(S, M):
    best_cost, choices = minBadDynamicChoice(S, M)
    if choices[-1] < max(choices): choices[-1] = choices[-2]
    i, j = 0, 0
    paragraph = ''
    while j < len(S):
        j = choices[i]
        for k in range(i,j):
            paragraph = paragraph + S[k] + ' '
        paragraph = paragraph + '\n'
        i = j

    print(paragraph)

#S = ['This','the','fuck','is','going','on','here','in']
S = "Ah how shameless – the way these mortals blame the gods. From us alone they say come " \
    "all their miseries yes but they themselves with their own reckless ways compound their pains " \
    "beyond their proper share"

S = S.split()
printParagraph(S,20)