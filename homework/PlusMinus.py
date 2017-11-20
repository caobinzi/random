from random import randint

MAX_NUM = 15


def pad(a):
    s = str(a)
    if len(s) == 1:
        return " " + s
    else:
        return s


def getRandome(mymin, mymax):
    return randint(mymin, mymax)


def getPlus(mymin, mymax):
    a = getRandome(mymin, mymax)
    b = getRandome(mymin, mymax)

    return pad(a) + " + " + pad(b) + " =    \t"


def max(a, b):
    if a > b:
        return a
    else:
        return b


def min(a, b):
    if a > b:
        return b
    else:
        return a


def getMinus(mymin, mymax):
    a = getRandome(mymin, mymax)
    b = getRandome(mymin, mymax)
    c = max(a, b)
    d = min(a, b)

    return pad(c) + " - " + pad(d) + " =    \t"


def writeFile(file_name, line):
    with open(file_name, "a") as myfile:
        myfile.write(line+"\n")

start = 1
end = 20

lines = [getPlus(start, end) + getPlus(start, end) + getMinus(start, end) for l in range(1, 200)]

for line in lines:
    writeFile("/Users/caobinzi/Desktop/a.txt", line)
