import utils as u

inputContents = u.reafile("../../../../inputs/day4.txt")


def isValid1(x):
    toks = x.split(" ")
    wordCount = len(toks)
    distinctWordCount = len(list(set(toks)))
    return wordCount == distinctWordCount



def isValid2(x):
    toks = list(map(lambda y: "".join(sorted(y)), x.split(" ")))
    wordCount = len(toks)
    distinctWordCount = len(list(set(toks)))
    return wordCount == distinctWordCount

print(len(list(filter(isValid1, inputContents.split("\n")))))
print(len(list(filter(isValid2, inputContents.split("\n")))))
