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


def dfs(g, s):
    graph = list_to_node_list(g)
    buf = dfs_stack(graph, s)
    for i in range(len(buf.graph)):
        if i != s and buf.graph[i].colour == 'white':
            buf = dfs_stack(buf.graph, i, buf.time + 1)

    return buf.graph
