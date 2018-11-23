import utils as u


def solve(inputContents, offset):
    inputLen = len(inputContents)
    resSum = 0
    for i in range(inputLen):
        nextI = (i + offset) % inputLen
        if inputContents[i] == inputContents[nextI]:
            resSum += int(inputContents[i])
    return resSum


def Main():
    inputContents = u.reafile("../../../../inputs/day1.txt")
    inputLen = len(inputContents)
    print(solve(inputContents, 1))
    print(solve(inputContents, int(inputLen / 2)))


if __name__ == '__main__':
    Main()
