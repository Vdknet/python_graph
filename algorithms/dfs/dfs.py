from collections import deque, namedtuple
from structures.simple import Node, Edge
import math


def list_to_node_list(g):
    graph = []
    for item in g:
        node = Node()
        node.adj = []
        for e in item:
            if isinstance(e, Edge):
                node.adj.append(e)
            else:
                node.adj.append(Edge(e))
        graph.append(node)
    return graph


def dfs_visit(g, s, time):
    # g - node list, s - entry node, number;
    time += 1
    g[s].d = time
    g[s].colour = 'gray'
    for n in g[s].adj:
        if isinstance(n, int):
            n = Edge(n)
        if g[n.num].colour == 'white':
            g[n.num].parent = s
            time = dfs_visit(g, n.num, time)
    g[s].colour = 'black'
    time += 1
    g[s].f = time
    return time


def dfs_rec(g, s):
    graph = list_to_node_list(g)
    time = 0
    if graph[s].colour == 'white':
        time = dfs_visit(graph, s, time)
    for item in graph:
        if item.colour == 'white':
            time = dfs_visit(graph, s, time)
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
            child = graph[u.node].adj[u.white_child].num
            if graph[child].colour == 'white':
                graph[child].parent = u.node
                item = StackItem(child, 0)
                q.append(item)

    GraphTime = namedtuple('GraphTime', 'graph time')
    result = GraphTime(graph, time)
    return result


def dfs(g, s):
    graph = list_to_node_list(g)
    buf = dfs_stack(graph, s)
    for i in range(len(buf.graph)):
        if i != s and buf.graph[i].colour == 'white':
            buf = dfs_stack(buf.graph, i, buf.time + 1)

    return buf.graph
