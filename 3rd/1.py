inputFile = open('input.txt','r')

def getPriorityValue(character):
    unicodeValue = ord(character)
    isLowerCaseLetter = unicodeValue >= 97 and unicodeValue <= 122
    isUpperCaseLetter = unicodeValue >= 65 and unicodeValue <= 90

    if (isLowerCaseLetter):
        return unicodeValue - 96
    elif (isUpperCaseLetter):
        return unicodeValue - 38
    else:
        return 0


def getIntersection(firstCompartment, secondCompartment):
    return set(firstCompartment).intersection(secondCompartment)


def getIntersection(firstElf, secondElf, thirdElf):
    return set(firstElf).intersection(secondElf).intersection(thirdElf)


def firstTask():
    result = 0
    for line in inputFile.readlines():
        clearLine = line.strip()
        elementsCount = len(clearLine)
        
        firstCompartment = clearLine[:elementsCount // 2]
        secondCompartment = clearLine[elementsCount // 2:]

        for element in getIntersection(firstCompartment, secondCompartment):
            result += getPriorityValue(element)

    return result


def secondTask():
    result = 0
    lines = inputFile.readlines()
    numberOfLines = len(lines)
    for i in range(0, numberOfLines, 3):
        firstElf = lines[i].strip()
        secondElf = lines[i + 1].strip()
        thirdElf = lines[i + 2].strip()

        for element in getIntersection(firstElf, secondElf, thirdElf):
            result += getPriorityValue(element)

    return result


print(firstTask())
print(secondTask())