file = open("Day1Input.txt", "r") 

first = int(file.readline())
second = int(file.readline())
third = int(file.readline())
count = 0

while True:
    line = file.readline()
 
    if not line:
        break

    forth = int(line.strip())

    A = first + second + third
    B = second + third + forth

    if A < B:
        count += 1

    first = second
    second = third
    third = forth

print( count)
