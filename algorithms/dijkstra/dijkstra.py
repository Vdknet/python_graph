from structures.simple import Node, Edge


def list_to_node_graph(g):
    graph = []
    for i in range(len(g)):
        graph.append(Node(i))

    for i in range(len(graph)):
        for e in g[i].keys():
            val = g[i].get(e)
            edge = Edge(e, val, graph[e])
            reverse_edge = Edge(i, val, graph[i])
            if edge not in graph[i].adj:
                graph[i].adj.append(edge)
            if reverse_edge not in graph[e].adj:
                graph[e].adj.append(reverse_edge)

    return graph


def extract_min(arr):
    arr.sort(key=lambda item: item.d)
    return arr.pop(0)


def relax(a, b, w):
    if b.d > a.d + w:
        b.d = a.d + w
        b.parent = a


def dijkstra(g, s):
    done_nodes = []
    q = list_to_node_graph(g)
    q[s].d = 0
    while q:
        u = extract_min(q)
        done_nodes.append(u)
        for adj in u.adj:
            relax(u, adj.node, adj.val)

    return done_nodes

