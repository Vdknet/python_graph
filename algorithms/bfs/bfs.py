from collections import deque
from structures.simple import Node, Edge


def bfs(g, s):
    # g - adj list, s - source node, number;
    graph = []
    for item in g:
        node = Node()
        node.adj = item
        graph.append(node)
    graph[s].colour = 'gray'
    graph[s].d = 0
    q = deque()
    q.append(s)
    while q:
        u = q.popleft()
        for n in graph[u].adj:
            if isinstance(n, int):
                n = Edge(n)
            if graph[n.num].colour == 'white':
                graph[n.num].colour = 'gray'
                graph[n.num].d = graph[u].d + n.val
                graph[n.num].parent = u
                q.append(n.num)
            graph[n.num].colour = 'black'
    return graph




