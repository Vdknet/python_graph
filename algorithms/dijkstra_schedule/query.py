import math
import random


class Query:
    def __init__(self, source, dest, band, bandstep, index=0):
        self.source = source
        self.dest = dest
        self.band = band
        self.subq = []
        self.index = index
        self.latency = 0
        k = math.ceil(band/bandstep)
        bufband = 0
        for i in range(k):
            b = bandstep
            if bufband + bandstep >= band:
                b = band - bufband
            bufband += bandstep
            self.subq.append(SubQuery(source, dest, self, i, b))

    def __hash__(self):
        return hash((self.source, self.dest, self.band, self.index))

    def __eq__(self, other):
        return (self.source, self.dest, self.band, self.index) == \
               (other.source, other.dest, other.band, other.index)

    def __ne__(self, other):
        return not(self == other)


class SubQuery:
    def __init__(self, source, dest, mainq, index, bandwidth):
        self.source = source
        self.dest = dest
        self.mainq = mainq
        self.index = index
        self.bandwidth = bandwidth

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


class QuerySet(list):
    def __init__(self):
        self.queries_list = []
        self.main_list = []
        self.additional_list = []

    def add_query_item(self, query):
        self.main_list.append(len(self.queries_list))
        self.queries_list.append(query)
        sub_list = []
        for i in range(len(query.subq)):
            sub_list.append(i)
        self.additional_list.append(sub_list)

    def pick_random_subquery(self):
        query_index = random.choice(self.main_list)
        query = self.queries_list[query_index]
        subq_index = self.additional_list[query_index].pop(0)
        if len(self.additional_list[query_index]) == 0:
            self.main_list.remove(query_index)
        return query.subq[subq_index]