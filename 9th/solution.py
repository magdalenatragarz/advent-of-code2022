inputFile = open('input.txt','r')

headLocation = [0, 0]
tailLocation = [0, 0]

tailSteps = []        
tailSteps.append([tailLocation[0], tailLocation[1]])

def moveHeadRight():
    headLocation[0] = headLocation[0] + 1

def moveHeadLeft():
    headLocation[0] = headLocation[0] - 1

def moveHeadDown():
    headLocation[1] = headLocation[1] - 1

def moveHeadUp():
    headLocation[1] = headLocation[1] + 1

def isTailTouchingHead():
    return abs(tailLocation[0] - headLocation[0]) <= 1 and abs(tailLocation[1] - headLocation[1]) <= 1

def isSameColumn():
    return tailLocation[0] == headLocation[0]

def isSameRow():
    return tailLocation[1] == headLocation[1]

def getTailStr():
    return "[" + str(tailLocation[0]) + ", " + str(tailLocation[1]) + "]"

def getHeadStr():
    return "[" + str(headLocation[0]) + ", " + str(headLocation[1]) + "]"

def moveTail():
    if (isTailTouchingHead()):  
        return False
    elif (isSameColumn()):
        isTailUnder = headLocation[1] > tailLocation[1]
        if (isTailUnder):
            tailLocation[1] = tailLocation[1] + 1
            return True
        else:
            tailLocation[1] = tailLocation[1] - 1
            return True
    elif (isSameRow()):
        isTailOnLeft = headLocation[0] > tailLocation[0]
        if (isTailOnLeft):
            tailLocation[0] = tailLocation[0] + 1
            return True
        else:
            tailLocation[0] = tailLocation[0] - 1
            return True
    else:
        isHeadHigher = headLocation[1] > tailLocation[1]
        isHeadOnRight = headLocation[0] > tailLocation[0]

        if (isHeadHigher and isHeadOnRight):
            tailLocation[0] = tailLocation[0] + 1
            tailLocation[1] = tailLocation[1] + 1
            return True
        elif (isHeadHigher == False and isHeadOnRight):
            tailLocation[0] = tailLocation[0] + 1
            tailLocation[1] = tailLocation[1] - 1
            return True
        elif (isHeadHigher == False and isHeadOnRight == False):
            tailLocation[0] = tailLocation[0] - 1
            tailLocation[1] = tailLocation[1] - 1
            return True
        elif (isHeadHigher and isHeadOnRight == False):
            tailLocation[0] = tailLocation[0] - 1
            tailLocation[1] = tailLocation[1] + 1
            return True
    return False

def isStepAlreadySaved(newTailLocation):
    for location in tailSteps:
        if (location[0] == newTailLocation[0] and location[1] == newTailLocation[1]):
            return True
    return False

for line in inputFile.readlines():
    move = line.split(" ")
    direction = move[0]
    stepsCount = eval(move[1])
    for i in range(1, stepsCount + 1):
        if (direction == 'R'):
            moveHeadRight()
        elif (direction == 'L'):
            moveHeadLeft()
        elif (direction == 'D'):
            moveHeadDown()
        elif (direction == 'U'):
            moveHeadUp()
        moveTail()
        newTailLocation = [tailLocation[0], tailLocation[1]]
        if (isStepAlreadySaved(newTailLocation) == False):
            tailSteps.append(newTailLocation)


print(len(tailSteps))
