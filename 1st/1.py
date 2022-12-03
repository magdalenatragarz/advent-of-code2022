inputFile = open('1-input.txt','r')

maxSum = 0
currentSum = 0
for line in inputFile.readlines():
    if line.strip():
        currentSum = currentSum + int(line)
    else:
        if (currentSum > maxSum):
            maxSum = currentSum
        currentSum = 0

if (currentSum > maxSum):
    maxSum = currentSum

print(maxSum)