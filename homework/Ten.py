from random import randint

MAX_NUM = 15


def pad(a):
    s = str(a)
    if len(s) == 1:
        return " " + s
    else:
        return s


def getRandome(max):
    return randint(0, max)


def getPlus():
    a = getRandome(MAX_NUM)
    b = getRandome(MAX_NUM)

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


def getMinus():
    a = getRandome(MAX_NUM)
    b = getRandome(MAX_NUM)
    c = max(a, b)
    d = min(a, b)

    return pad(c) + " - " + pad(d) + " =    \t"


def writeFile(file_name, line):
    with open(file_name, "a") as myfile:
        myfile.write(line+"\n")


lines = [getPlus() + getPlus() + getMinus() for l in range(1, 216)]

for line in lines:
    writeFile("/Users/caobinzi/Desktop/a.txt", line)
