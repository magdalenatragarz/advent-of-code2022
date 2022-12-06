inputFile = open('input.txt','r')

buffer = inputFile.readline()

def task(markerSize):
    for i in range(0, len(buffer) - markerSize):
        posibbleMarker = buffer[i : i + markerSize]
        markerStringWithoutRepetitions = ''.join(set(posibbleMarker))
        if (len(markerStringWithoutRepetitions) == markerSize):
            return i + markerSize

print(task(4))
print(task(14))