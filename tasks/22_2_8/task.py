from structures.simple import Tree, Edge, Node
from algorithms.bfs.bfs import bfs
from collections import deque
import math


def tree_to_graph(tree):
    graph = []
    q = deque()
    q.append(tree.node)
    f = 0
    index = 0
    while q:
        u = q.popleft()
        graph.append(u)
        print(u)
        if not u.adj[0] is None:
            q.append(u.adj[0])
            f += 1
            u.adj[0] = index + f
        if not u.adj[1] is None:
            q.append(u.adj[0])
            f += 1
            u.adj[1] = index + f

        index += 1
        f = 0
    return graph


def reverse_graph(graph):
    rev_graph = []
    for i in range(len(graph)):
        u = Node()
        rev_graph.append(u)

    for i in range(len(graph)):
        for j in graph[i].adj:
            if isinstance(j, int):
                j = Edge(j)
            e = Edge(i, j.val)
            rev_graph[j.num].adj.append(e)
    return rev_graph


def max_path(graph):
    path = 0
    index = None
    for i in range(len(graph)):
        if graph[i].d >= path and graph[i].d != math.inf:
            path = graph[i].d
            index = i
    return [path, index]


def tree_dia(graph):
    far_source = max_path(bfs(graph, 0))[1]
    diameter = max_path(bfs(graph, far_source))[0]
    return diameter


