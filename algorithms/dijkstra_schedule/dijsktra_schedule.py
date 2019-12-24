from structures.simple import Node, Edge
from .query import Query
from .schedule import Schedule
import math


def list_to_node_graph(g):
    graph = []
    for i in range(len(g)):
        graph.append(Node(i))

    for i in range(len(g)):
        for e in g[i]:
            edge = Edge(e, 0, graph[e])
            reverse_edge = Edge(i, 0, graph[i])
            if edge not in graph[i].adj:
                graph[i].adj.append(edge)
            if reverse_edge not in graph[e].adj:
                graph[e].adj.append(reverse_edge)

    return graph


def extract_min(arr):
    arr.sort(key=lambda item: item.d)
    return arr.pop(0)


def relax(a, b, t, h):
    n = h.nearest_step(a.index, b.index, t)
    if n is not None and (b.d > n or b.d is math.inf):
        b.d = n
        b.parent = a
    return n


def dijkstra_route(g, s, d, h):
    done_nodes = []
    q = list_to_node_graph(g)
    q[s].d = 0
    while q:
        u = extract_min(q)
        done_nodes.append(u)
        for adj in u.adj:
            relax(u, adj.node, u.d, h)

    done_nodes.sort(key=lambda item: item.index)
    cur = done_nodes[d]
    par = cur.parent
    result = []
    if par is None:
        return None
    else:
        while par is not None:
            result.append({'s': par.index, 'd': cur.index, 't': cur.d})
            cur = par
            par = done_nodes[par.index].parent
        return result


def dijkstra_schedule(queries, graph):
    h = Schedule()
    for i in range(len(queries)):
        q = queries[i]
        s = q.get('s')
        d = q.get('d')
        b = q.get('b')
        big_q = Query(s, d, b, 100, i)
        sub_queries = big_q.subq
        for j in range(len(sub_queries)):
            sq = sub_queries[j]
            path = dijkstra_route(graph, sq.source, sq.dest, h)
            if path is not None:
                for e in reversed(path):
                    h.write_one(e.get('s'), e.get('d'), e.get('t'), sq)
    return h




