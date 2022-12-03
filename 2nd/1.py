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

yourRock = "X"
yourPaper = 'Y'
yourScissors = 'Z'

def getResultOfMove(opponentsMove, yourMove):
    if (opponentsMove == opponentRock and yourMove == yourRock):
        return drawPoints + rockPoints
    if (opponentMove == opponentPaper and yourMove == yourPaper):
        return drawPoints + paperPoints
    if (opponentMove == opponentScissors and yourMove == yourScissors):
        return drawPoints + scissorsPoints

    if (opponentMove == opponentRock and yourMove == yourPaper):
        return winPoints + paperPoints
    if (opponentMove == opponentPaper and yourMove == yourScissors):
        return winPoints + scissorsPoints
    if (opponentMove == opponentScissors and yourMove == yourRock):
        return winPoints + rockPoints
        
    if (opponentMove == opponentRock and yourMove == yourScissors):
        return lossPoints + scissorsPoints
    if (opponentMove == opponentPaper and yourMove == yourRock):
        return lossPoints + rockPoints
    if (opponentMove == opponentScissors and yourMove == yourPaper):
        return lossPoints + paperPoints
        
    return 0
        

result = 0
for line in inputFile.readlines():
    moves = line.split(" ")
    opponentMove = moves[0]
    yourMove = moves[1]
    yourMove = yourMove.replace('\n', "")
    opponentMove = opponentMove.replace('\n', "")
    
    result = result + getResultOfMove(opponentMove, yourMove)
    

print(result)

