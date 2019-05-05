from collections import deque, namedtuple
from structures.simple import Node, Edge
import math


def add_inverse_edges(graph):
    for i in range(len(graph)):
        for e in graph[i].adj:
            graph[e.num].adj.append(Edge(i))
    return graph


def reverse_graph(graph):
    rev_graph = []
    for i in range(len(graph)):
        u = Node()
        u.num = i
        rev_graph.append(u)

    for i in range(len(graph)):
        for j in graph[i].adj:
            if isinstance(j, int):
                j = Edge(j)
            e = Edge(i, j.val)
            rev_graph[j.num].adj.append(e)
    return rev_graph


def list_to_node_list(g):
    graph = []
    for i in range(len(g)):
        node = Node()
        node.adj = []
        for e in g[i]:
            if isinstance(e, Edge):
                node.adj.append(e)
            else:
                node.adj.append(Edge(e))
        graph.append(node)
    return graph


def dfs_stack(graph, s, time=1):
    graph[s].d = time
    graph[s].colour = 'gray'
    q = deque()
    StackItem = namedtuple('StackItem', 'node white_child')
    item = StackItem(s, 0)
    q.append(item)
    while q:
        u = q.pop()
        if graph[u.node].d == math.inf:
            time += 1
            graph[u.node].d = time
        graph[u.node].colour = 'gray'
        if u.white_child >= len(graph[u.node].adj):
            graph[u.node].colour = 'black'
            time += 1
            graph[u.node].f = time
        else:
            item = StackItem(u.node, u.white_child + 1)
            q.append(item)
            child = graph[u.node].adj[u.white_child]
            if graph[child.num].colour == 'white':
                child.type = 'tree edge'
                graph[child.num].parent = u.node
                item = StackItem(child.num, 0)
                q.append(item)
            elif graph[child.num].colour == 'gray':
                child.type = 'back edge'
            elif graph[child.num].colour == 'black':
                if graph[child.num].d > graph[u.node].d:
                    child.type = 'forward edge'
                else:
                    child.type = 'cross edge'

    GraphTime = namedtuple('GraphTime', 'graph time')
    result = GraphTime(graph, time)
    return result


def find_comp(g):
    graph = list_to_node_list(g)
    buf = dfs_stack(reverse_graph(graph), 0)
    for i in range(len(buf.graph)):
        if buf.graph[i].colour == 'white':
            buf = dfs_stack(buf.graph, i, buf.time + 1)

    sorted(buf.graph, key=lambda item: item.f)
    cc = 0
    GraphTime = namedtuple('GraphTime', 'graph time')
    result = GraphTime(add_inverse_edges(graph), 0)
    for item in buf.graph:
        if result.graph[item.num].colour == 'white':
            cc += 1
            result = dfs_stack(result.graph, item.num, result.time + 1)

        result.graph[item.num].cc = cc

    return result.graph
