import math


class Query:
    def __init__(self, source, dest, band, bandstep, index=0):
        self.source = source
        self.dest = dest
        self.band = band
        self.subq = []
        self.index = index
        k = math.ceil(band/bandstep)
        for i in range(k):
            self.subq.append(SubQuery(source, dest, self, i))

    def __hash__(self):
        return hash((self.source, self.dest, self.band, self.index))

    def __eq__(self, other):
        return (self.source, self.dest, self.band, self.index) == \
               (other.source, other.dest, other.band, other.index)

    def __ne__(self, other):
        return not(self == other)


class SubQuery:
    def __init__(self, source, dest, mainq, index):
        self.source = source
        self.dest = dest
        self.mainq = mainq
        self.index = index

    def __str__(self):
        return "\n{source: " + str(self.source) +\
               ", dest:" + str(self.dest) + "}"

    def __hash__(self):
        return hash((self.source, self.dest, self.mainq, self.index))

    def __eq__(self, other):
        return (self.source, self.dest, self.mainq, self.index) == \
               (other.source, other.dest, other.mainq, other.index)

    def __ne__(self, other):
        return not(self == other)
