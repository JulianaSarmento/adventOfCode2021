file = open("Day02Input.txt", "r") 

depth = 0 
horizontal = 0
while True:
    line = file.readline()

    if not line:
        break

    lineParts = line.split(" ")

    if lineParts[0] == "forward":
       horizontal += int(lineParts[1])
    elif lineParts[0] == "down":
        depth += int(lineParts[1])
    elif lineParts[0] == "up":
        depth -= int(lineParts[1])
    else:
        print('error1')
        break
    if depth < 0:
        print('error2')
        break

print( depth)
print( horizontal)
print( depth * horizontal)
file.close()

file = open("Day02Input.txt", "r") 
aim = 0 
horizontal = 0
depth = 0
while True:
    line = file.readline()

    if not line:
        break

    lineParts = line.split(" ")

    if lineParts[0] == "forward":
        horizontal += int(lineParts[1])
        depth += int(lineParts[1]) * aim
    elif lineParts[0] == "down":
        aim += int(lineParts[1])
    elif lineParts[0] == "up":
        aim -= int(lineParts[1])
    else:
        print('error1')
        break

print(depth)
print(horizontal)
print(depth * horizontal)
file.close()

