import sys


def doNothing():
    return


def main(filename):
    with open(filename, 'r') as file:
        sum = 0
        for line in file:
            maxl = int(line[0])
            maxr = int(line[1])
            print(maxl, maxr, end="", sep="")
            for i in range(1, len(line) - 1):
                print(line[i], sep="", end="")
                val = int(line[i])
                if maxl < val and i < len(line) - 2:
                    maxl = val
                    maxr = int(line[i+1])
                elif maxr < val:
                    maxr = val
            print("")
            print(maxl, maxr, end="", sep="")
            print("")

            sum += int(str(maxl) + str(maxr))
        print(sum)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    main(filename)
