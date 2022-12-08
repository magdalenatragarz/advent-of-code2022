inputFile = open('input.txt','r')

forest = []

for line in inputFile.readlines():
    line = line.strip()
    row = [int(x) for x in line]
    forest.append(row)

rowsNumber = len(forest)
columnsNumber = len(forest[0])

def isTreeVisibleFromLeft(x, y):
    for i in range(0, x):
        if forest[y][i] >= forest[y][x]:
            return False
    return True

def isTreeVisibleFromRight(x, y):
    for i in range(x + 1, columnsNumber):
        if forest[y][i] >= forest[y][x]:
            return False
    return True

def isTreeVisibleFromTop(x, y):
    for i in range(0, y):
        if forest[i][x] >= forest[y][x]:
            return False
    return True

def isTreeVisibleFromBottom(x, y):
    for i in range(y + 1, rowsNumber):
        if forest[i][x] >= forest[y][x]:
            return False
    return True

visibleCount = rowsNumber * 2 + (columnsNumber - 2) * 2

for x in range(1, columnsNumber - 1):
    for y in range(1, rowsNumber - 1):
        isTreeVisibleInRow = isTreeVisibleFromLeft(x, y) or isTreeVisibleFromRight(x, y)
        isTreeVisibleInColumn = isTreeVisibleFromTop(x, y) or isTreeVisibleFromBottom(x, y)
        if (isTreeVisibleInRow or isTreeVisibleInColumn):
            visibleCount += 1

def getBottomScenicScore(x, y):
    scenicScore = 0
    for i in range(y + 1, rowsNumber):
        scenicScore += 1
        if forest[i][x] >= forest[y][x]:
            return scenicScore
    return scenicScore

def getTopScenicScore(x, y):
    scenicScore = 0
    for i in range(y - 1, -1, -1):
        scenicScore += 1
        if forest[i][x] >= forest[y][x]:
            return scenicScore
    return scenicScore

def getRightScenicScore(x, y):
    scenicScore = 0
    for i in range(x + 1, columnsNumber):
        scenicScore += 1
        if forest[y][i] >= forest[y][x]:
            return scenicScore
    return scenicScore

def getLeftScenicScore(x, y):
    scenicScore = 0
    for i in range(x - 1, -1, -1):
        scenicScore += 1
        if forest[y][i] >= forest[y][x]:
            return scenicScore
    return scenicScore

maxScenicScore = 0
for x in range(1, columnsNumber - 1):
    for y in range(1, rowsNumber - 1):
        scenicScore = getLeftScenicScore(x, y) * getRightScenicScore(x, y) * getTopScenicScore(x, y) * getBottomScenicScore(x, y)
        if (scenicScore > maxScenicScore):
            maxScenicScore = scenicScore


print(maxScenicScore)
