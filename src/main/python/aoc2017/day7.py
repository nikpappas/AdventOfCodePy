from anytree import Node, RenderTree
import utils as u


class MyNode(Node):
    def __init__(self, name, parent, weight):
        super().__init__(name, parent)
        self.weight = weight


def parseNodes(str):
    toks = str.split(" ")
    name = toks[0]
    weight = int(toks[1].replace("(","").replace(")",""))
    if len(toks) > 2:
        return MyNode(name, None, weight)
    else:
        return MyNode(name, None, weight)


def Main():
    inputContents = u.reafile("../../../../inputs/day7.txt")
    instructions = list(map(parseNodes, (inputContents.split("\n"))))
    print(instructions)


if __name__ == '__main__':
    Main()
