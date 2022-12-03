inputFile = open('input.txt','r')

winPoints = 6
drawPoints = 3
lossPoints = 0

rockPoints = 1
paperPoints = 2
scissorsPoints = 3

opponentRock = "A"
opponentPaper = 'B'
opponentScissors = 'C'

loseResult = "X"
drawReslt = 'Y'
winResult = 'Z'

def getResultOfMove(opponentsMove, expectedResult):
    if (opponentsMove == opponentRock and expectedResult == drawReslt):
        return drawPoints + rockPoints
    if (opponentMove == opponentPaper and expectedResult == drawReslt):
        return drawPoints + paperPoints
    if (opponentMove == opponentScissors and expectedResult == drawReslt):
        return drawPoints + scissorsPoints

    if (opponentMove == opponentRock and expectedResult == winResult):
        return winPoints + paperPoints
    if (opponentMove == opponentPaper and expectedResult == winResult):
        return winPoints + scissorsPoints
    if (opponentMove == opponentScissors and expectedResult == winResult):
        return winPoints + rockPoints
        
    if (opponentMove == opponentRock and expectedResult == loseResult):
        return lossPoints + scissorsPoints
    if (opponentMove == opponentPaper and expectedResult == loseResult):
        return lossPoints + rockPoints
    if (opponentMove == opponentScissors and expectedResult == loseResult):
        return lossPoints + paperPoints
        
    return 0
        

result = 0
for line in inputFile.readlines():
    moves = line.split(" ")
    opponentMove = moves[0]
    expectedResult = moves[1]
    expectedResult = expectedResult.replace('\n', "")
    opponentMove = opponentMove.replace('\n', "")
    
    result = result + getResultOfMove(opponentMove, expectedResult)
    

print(result)

