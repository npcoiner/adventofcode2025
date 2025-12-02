import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "input.txt"
with open(filename, 'r') as file:
    clicks = 0
    number = 50
    for line in file:
        if line != "":
            value = int(line[1::])
            letter = line[0]
            fullRotas = value // 100

            if letter == "R":
                number += (value % 100)
                if number >= 100:
                    clicks += 1
            else:
                if (number == 0):
                    number += 100
                number -= abs(value) % 100
                if number <= 0:
                    clicks += 1
            clicks += fullRotas
            number = number % 100
            print(letter, value, "dial: ", number, "total:", clicks, sep=" ")
        else:
            break
    print(clicks)
