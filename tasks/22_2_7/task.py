from collections import deque
from structures.simple import Node, Edge


def list_to_node_list(g):
    graph = []
    for item in g:
        node = Node()
        node.adj = item
        graph.append(node)
    return graph



def bfs_visit(graph, s):
    # graph - node list, s - source node, number;
    graph[s].colour = 'first'
    graph[s].d = 0
    q = deque()
    q.append(s)
    while q:
        u = q.popleft()
        for n in graph[u].adj:
            if isinstance(n, int):
                n = Edge(n)
            if graph[n.num].colour == 'white':
                graph[n.num].colour = 'second' if graph[u].colour == 'first' \
                    else 'first'
                graph[n.num].d = graph[u].d + n.val
                graph[n.num].parent = u
                q.append(n.num)
            elif graph[n.num].colour == graph[u].colour:
                return -1
    return graph


def bfs_double_colouring(g, s):
    g = bfs_visit(g, s)
    for i in range(len(g)):
        if isinstance(g, int) and g == -1:
            return g
        if i != s and g[i].colour == 'white':
            g = bfs_visit(g, i)

    return g

