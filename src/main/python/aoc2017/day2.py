from re import split

import utils as u

inputContents = u.reafile("../../../../inputs/day2.txt")


def parseContents(contents):
    lines = split("\n", contents)
    tokenised = list(map(lambda l: split("\t", l), lines))
    return (list(map(int, l)) for l in tokenised)


def minMaxDiff(line):
    return max(line) - min(line)


spreadSheet = parseContents(inputContents)


def divideDivisible(line):
    for n in line:
        for m in line:
            if m is not n and n % m is 0:
                return n / m


a = [minMaxDiff(line) for line in spreadSheet]
print(sum(a))

spreadSheet = parseContents(inputContents)
b = [divideDivisible(line) for line in spreadSheet]
print(sum(b))
