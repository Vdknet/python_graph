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
    def __init__(self, num, val=1, edge_type=None):
        self.num = num
        self.val = val
        self.type = edge_type

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{ " + ", ".join("%s: %s" % item for item in vars(self).items())\
               + "}"


class Tree:
    def __init__(self, node=None, left=None, right=None):
        self.node = node
        self.node.adj = [left, right]
