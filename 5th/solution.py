from queue import Queue

procedureFile = open('procedure.txt','r')
stacksFile = open('current-stacks.txt', 'r')

stacksCount = 9
chunkSize = 4

stacks = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],
    8 : [],
    9 : []
}

def getChunkedLine(line):
    chunkedLine = []
    for i in range (0, len(line), chunkSize):
        chunkedLine.append(line[i: i + chunkSize].strip())
    return chunkedLine


def fillStacksArray(chunkedLine):
    stackId = 1
    for chunk in chunkedLine:
        if (chunk):
            stacks[stackId].append(chunk.split('[')[1].split(']')[0])
        stackId += 1 


def getCount(line):
    return eval(line.split('from')[0].split(" ")[1])


def getSource(line):
    return eval(line.split('from')[1].split(" to ")[0])


def getDestination(line):
    return eval(line.split('from')[1].split(" to ")[1])


def firstTask():
    for line in procedureFile.readlines():
        count = getCount(line)
        source = getSource(line)
        destination = getDestination(line)
        for i in range(0, count):
            toBeMoved = stacks[source].pop(0)
            stacks[destination].insert(0, toBeMoved)


def secondTask():
    for line in procedureFile.readlines():
        count = getCount(line)
        source = getSource(line)
        destination = getDestination(line)

        toBeMoved = stacks[source][0:count]
        stacks[source] = stacks[source][count:]
        stacks[destination][0:0] = toBeMoved


for line in stacksFile.readlines():
    chunkedLine = getChunkedLine(line)
    fillStacksArray(chunkedLine)

secondTask()

for stackId in stacks:
    print(stacks[stackId][0])

