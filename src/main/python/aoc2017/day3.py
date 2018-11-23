from functools import partial

INPUT = 347991


# Directions 0:East, 1:North, 2:West, 3:South

class Entry:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y
        self.val2 = 0


class Memory:
    def __init__(self):
        self.mem = []
        self.dirVectors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.sidelength = 0

    def createLayers(self, i=0):
        if i is 0:
            e = Entry(1, 0, 0)
            e.val2 = 1
            self.mem.append(e)

            return self.createLayers(1)
        index = i
        for direction in range(4):
            if direction % 2 is 0:
                self.sidelength = self.sidelength + 1
            for _ in range(self.sidelength):
                if index >= INPUT: return
                dirVec = self.dirVectors[direction]
                prev = self.mem[index - 1]
                x = prev.x + dirVec[0]
                y = prev.y + dirVec[1]
                val = self.findVal1(index)
                self.mem.append(Entry(val, x, y))
                # Second Stage -- Comment to run first stage
                val2 = self.findVal2(index)
                self.mem[index].val2 = val2
                if val2 > INPUT: return
                # Second Stage second stage end
                index = index + 1
        self.createLayers(index)

    def findVal1(self, index):
        return self.mem[index - 1].val + 1

    def findVal2(self, index):
        e = list(filter(partial(self.findNeighbours, index), self.mem))
        values = list(map(lambda x: x.val2, e))
        return sum(values)

    def findNeighbours(self, index, x):
        cur = self.mem[index]
        coordDistX = findCoordDist(cur.x, x.x)
        coordDistY = findCoordDist(cur.y, x.y)
        if coordDistX > 1: return False
        if coordDistY > 1: return False
        return True


def findCoordDist(curCord, itCord):
    return abs(curCord - itCord)


mem = Memory()
mem.createLayers()

finalX = mem.mem[len(mem.mem) - 1].x
finalY = mem.mem[len(mem.mem) - 1].y
manhattanDist = abs(finalX) + abs(finalY)
print(manhattanDist)
print(mem.mem[len(mem.mem) - 1].val2)