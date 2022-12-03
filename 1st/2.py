inputFile = open('1-input.txt','r')

calories = []

currentSum = 0
for line in inputFile.readlines():
    if line.strip():
        currentSum = currentSum + int(line)
    else:
        calories.append(currentSum)
        currentSum = 0

calories.append(currentSum)
calories.sort(reverse=True)

print(calories[0] + calories[1] + calories[2])