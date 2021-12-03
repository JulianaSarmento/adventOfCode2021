file = open("Day03Input.txt", "r") 

count0 = [0,0,0,0,0,0,0,0,0,0,0,0]
count1 = [0,0,0,0,0,0,0,0,0,0,0,0]

while True:
    line = file.readline()

    if not line:
        break

    i=0
    for char in line:
        if(char == "0"):
            count0[i] += 1
        elif(char == "1"):
            count1[i] += 1
        i += 1 

file.close()
print(count0)
print(count1)

gamma = ["0","0","0","0","0","0","0","0","0","0","0","0"]
epsilon = ["0","0","0","0","0","0","0","0","0","0","0","0"]

for x in range(12):
    if (count0[x]>count1[x]):
        epsilon[x] = "1"
    else:
        gamma[x] = "1"

print(gamma)
print(epsilon)

gammaString = ''.join(gamma)
epsilonString = ''.join(epsilon) 

gammaDecimal = int(gammaString, 2)
epsilonDecimal = int(epsilonString, 2)

print(gammaDecimal)
print(epsilonDecimal)

print(gammaDecimal * epsilonDecimal)

oxygen = [0,0,0,0,0,0,0,0,0,0,0,0]

file = open("Day03Input.txt", "r") 

i= 0
lines=[]
count0 = 0
count1 = 0
while True:
    line = file.readline()

    if not line:
        break

    lines.append(line.strip())

linesOxygen = lines
linesCO2 = lines 
for x in range(12):
    if len(linesOxygen) == 1:
        break
    count0 = 0
    count1 = 0
    for line in linesOxygen:
        if line[x] == "0":
            count0 += 1
        else:
            count1 += 1
    newLines = []
    if count0 > count1:
        for line in linesOxygen:
            if line[x] == "0":
                newLines.append(line)
    else: 
        for line in linesOxygen:
            if line[x] == "1":
                newLines.append(line)
    linesOxygen = newLines

for x in range(12):
    if len(linesCO2) == 1:
        break
    count0 = 0
    count1 = 0
    for line in linesCO2:
        if line[x] == "0":
            count0 += 1
        else:
            count1 += 1
    newLines = []
    if count0 > count1:
        for line in linesCO2:
            if line[x] == "1":
                newLines.append(line)
    else: 
        for line in linesCO2:
            if line[x] == "0":
                newLines.append(line)
    linesCO2 = newLines

print(linesCO2)
print(linesOxygen)

oxygenDecimal = int(linesOxygen[0], 2)
co2Decimal = int(linesCO2[0], 2)

print(oxygenDecimal * co2Decimal)