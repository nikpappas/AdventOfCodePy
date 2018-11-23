import utils as u

inputContents = u.reafile("../../../../inputs/day6.txt")
instructions = list(map(lambda x: int(x), (inputContents.split("\t"))))

# instructions = [0, 2, 7, 0] #TEST

instructionHistory = []
print(instructions)


def listsEqual(a, b):
    for i in range(len(a)):
        if a[i] != b[i]: return False
    return True


def existsInHistory(a):
    for entry in instructionHistory:
        if listsEqual(entry, a):
            return True
    return False


def increment(index):
    return (index + 1) % len(instructions)


count = 0
instLen = len(instructions)

while not existsInHistory(instructions):
    count = count + 1
    maxElem = max(instructions)
    index = instructions.index(maxElem)

    instructionHistory.append(instructions.copy())
    carry = instructions[index]
    instructions[index] = 0

    for i in range(carry):
        index = increment(index)
        instructions[index] = instructions[index] + 1
    # print(instructions)
    if count % 1000 == 0:
        print(count)

print(count)


def indexOf(a):
    for i in range(len(instructionHistory)):
        if listsEqual(instructionHistory[i], a):
            return i
    return -1


print("2nd stage")
print(count - indexOf(instructions))


#  TESTS
# def testExistInHistory():
#     ones = [1,1,1]
#     instructionHistory.append(ones)
#     print(existsInHistory(ones))
#
# testExistInHistory()
