import math


class Node:
    def __init__(self):
        self.colour = 'white'
        self.d = math.inf
        self.f = math.inf
        self.parent = None
        self.adj = []

    def __str__(self):
        return "\n{ clr:" + str(self.colour) + \
               ", d:" + str(self.d) + \
               ", f:" + str(self.f) + \
               ", parent:" + str(self.parent) + \
                 ", adj:" + str(self.adj) + "}"

    def __repr__(self):
        return str(self)



class Edge:
    def __init__(self, num, val=1):
        self.num = num
        self.val = val

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{ neighbour: " + str(self.num) + \
               ", value: " + str(self.val) + "}"


class Tree:
    def __init__(self, node=None, left=None, right=None):
        self.node = node
        self.node.adj = [left, right]
