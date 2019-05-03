from structures.simple import Node, Edge


def dfs_visit(g, s, time):
    # g - adj list, s - entry node, number;
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


def dfs(g, s):
    graph = []
    time = 0
    for item in g:
        node = Node()
        node.adj = item
        graph.append(node)

    time = dfs_visit(graph, s, time)
    return graph
