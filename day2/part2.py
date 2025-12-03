import sys


def doNothing(x):
    return


def doInRange(left, right, function=doNothing):
    count = 0
    for i in range(int(left), int(right + 1)):
        function(i)
        count += 1
    return count


def isFactor(factor, number):
    if number % factor == 0:
        return True
    else:
        return False


def main(filename):
    with open(filename, 'r') as file:
        sum = 0
        for line in file:
            splitcomma = line.split(",")
            for split in splitcomma:
                id_range = split.split("-")
                left = int(id_range[0])
                right = int(id_range[1])

                print(doInRange(left, right))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    main(filename)
