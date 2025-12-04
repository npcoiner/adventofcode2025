import sys


def doNothing():
    print("")
    return


def main(filename):
    with open(filename, 'r') as file:
        sum = 0
        for line in file:
            print(line)
            maxl = int(line[0])
            maxr = int(line[1])

            for i in line:
                try:
                    print(int(i))
                except ValueError:
                    doNothing()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    main(filename)
