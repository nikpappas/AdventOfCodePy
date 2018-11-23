import utils as u

inputContents = u.reafile("../../../../inputs/day5.txt")
instructions = list(map(lambda x: int(x), (inputContents.split("\n"))))


def move(index):
    return index + instructions[index]


def increment(index):
    instructions[index] = instructions[index] + 1


def decrement(index):
    instructions[index] = instructions[index] - 1


def iterate():
    count = 0
    index = 0
    while index < len(instructions) and index >= 0:
        newIndex = move(index)
        increment(index)
        count = count + 1
        index = newIndex
    return count


def increment2(index):
    if instructions[index] >= 3:
        decrement(index)
    else:
        increment(index)


def iterate2():
    count = 0
    index = 0
    while len(instructions) > index >= 0:
        newIndex = move(index)
        increment2(index)
        count = count + 1
        index = newIndex
    return count


print(instructions)
print(len(instructions))
print(str(iterate2()))
