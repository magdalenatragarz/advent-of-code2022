inputFile = open('input.txt','r')

def firstTask():
    result = 0
    for line in inputFile.readlines():
        ranges = line.split(",")
        
        firstElfRange = ranges[0].split("-")
        secondElfRange = ranges[1].split("-")

        firstElfRange = [eval(i) for i in firstElfRange]
        secondElfRange = [eval(i) for i in secondElfRange]

        doesFirstFullyContainSecond = firstElfRange[0] <= secondElfRange[0] and firstElfRange[1] >= secondElfRange[1]
        doesSecondFullyContainFirst =  secondElfRange[0] <= firstElfRange[0] and secondElfRange[1] >= firstElfRange[1]

        if (doesFirstFullyContainSecond or doesSecondFullyContainFirst):
            result += 1

    return result


def secondTask():
    result = 0
    for line in inputFile.readlines():
        ranges = line.split(",")
        
        firstElfRange = ranges[0].split("-")
        secondElfRange = ranges[1].split("-")

        firstElfRange = [eval(i) for i in firstElfRange]
        secondElfRange = [eval(i) for i in secondElfRange]
        
        firstElfRangeList = []
        secondElfRangeList = []

        firstElfRangeList.extend(range(firstElfRange[0], firstElfRange[1] + 1))
        secondElfRangeList.extend(range(secondElfRange[0], secondElfRange[1] + 1))

        intersection = set(firstElfRangeList) & set(secondElfRangeList)

        if (len(intersection) != 0):
            result += 1

    return result

print(secondTask())
