import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "input.txt"


def testNumber(number, left, right):
    number = int(number)
    combined = int(str(number) + str(number))
    sum = 0
    print("range", left, right, number)
    while (combined < int(right)):
        if (combined > int(left)):
            print(combined, end=',')
            sum += combined
        number += 1
        combined = int(str(number) + str(number))

    print("")
    return sum


with open(filename, 'r') as file:
    sum = 0
    for line in file:
        splitcomma = line.split(",")
        for split in splitcomma:
            id_range = split.split("-")
            left = id_range[0]
            right = id_range[1]

            number = ""

            singleton = ""
            padding = 0
            digits = 0

            if (len(left) % 2 == 0):
                digits = len(left) // 2
                padding = 0
                number = number + left[:digits:]

            else:
                digits = len(left) // 2

                number = str(10**(digits))

            sum += testNumber(number, left, right)
            print(sum)
            print("\n")
