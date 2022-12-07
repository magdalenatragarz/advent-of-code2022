from anytree import Node, RenderTree

inputFile = open('input.txt','r')

def isChangeLevelCommand(line):
    return line.startswith("$ cd")

def isListCommand(line):
    return line == "$ ls"

def isDirectory(line):
    return line.startswith("dir")

def parseInputFile():
    currentLevel = Node("/")
    root = currentLevel
    for line in inputFile.readlines():
        line = line.strip()
        if (isChangeLevelCommand(line)):
            newLevelName = line[5:]
            newLevelName = newLevelName.strip()
            if (newLevelName == ".."):
                newLevel = currentLevel.parent
                currentLevel = newLevel
            else:
                alreadyExists = False
                newFileName = "dir " + newLevelName
                for child in currentLevel.children:
                    if (child.name == newFileName):
                        currentLevel = child
                        alreadyExists = True
                        break
                if (not alreadyExists):
                    newLevel = Node(newFileName, parent=currentLevel)
                    currentLevel = newLevel
        elif (isListCommand(line)):
            continue
        else:
            alreadyExists = False
            for child in currentLevel.children:
                if (child.name == line):
                    alreadyExists = True
                    break
            if (not alreadyExists):
                newLevel = Node(line, parent=currentLevel)

    return root

def getSizeOfChildren(dirNode):
    size = 0
    for child in dirNode.children:
        if (isDirectory(child.name)):
            size += getSizeOfChildren(child)
        else:
            size += eval(child.name.split(" ")[0])
    return size

root = parseInputFile()

    
totalSize = 0
for _, _, node in RenderTree(root):
    if (isDirectory(node.name)):
        size = getSizeOfChildren(node)
        if (size < 100000):
            totalSize += size
            #print("Size of " + node.name + " is " + str(size))


diskSize = 70000000
spaceNeededForUpdate = 30000000

currentUsedSpace = getSizeOfChildren(root)
currentFreeSpace = diskSize - currentUsedSpace

spaceToBeFreed = spaceNeededForUpdate - currentFreeSpace

print(spaceToBeFreed)

minToBeDeleted = currentUsedSpace
for _, _, node in RenderTree(root):
    if (isDirectory(node.name)):
        size = getSizeOfChildren(node)
        if (size >= spaceToBeFreed and size < minToBeDeleted):
            minToBeDeleted = size

print(minToBeDeleted)

#for pre, fill, node in RenderTree(root):
#    print("%s%s" % (pre, node.name))