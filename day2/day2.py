import sys


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "input.txt"
with open(filename, 'r') as file:
    sum = 0
    for line in file:
        splitcomma = line.split(",")
        for split in splitcomma:
            id_range = split.split("-")
            left = int(id_range[0])
            right = int(id_range[1])

            print(left, right, sep=" ")
