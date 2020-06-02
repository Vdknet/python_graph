import itertools
import math

from structures.simple import Node, Edge
from .query import Query, QuerySet
from .schedule import Schedule


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
            if u.d is not math.inf:
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
    h_all = []
    for j in range(math.floor(len(queries)/2)):
        h = Schedule()
        q_set = QuerySet()
        sum_latency = 0
        for i in range(len(queries)):
            q = queries[i]
            s = q.get('s')
            d = q.get('d')
            b = q.get('b')
            h.requested += b
            big_q = Query(s, d, b, 100, i)
            q_set.add_query_item(big_q)

        while len(q_set.main_list) > 0:
            sq = q_set.pick_random_subquery()
            path = dijkstra_route(graph, sq.source, sq.dest, h)
            if path is not None:
                h.submitted += sq.bandwidth
                latency = path[0].get('t')
                if latency > sq.mainq.latency:
                    sq.mainq.latency = latency
                for e in reversed(path):
                    h.write_one(e.get('s'), e.get('d'), e.get('t'), sq)

        for q in q_set.queries_list:
            sum_latency += q.latency
            if h.max_latency < q.latency:
                h.max_latency = q.latency

        h.average_latency = sum_latency/len(queries)
        h_all.append(h)

    h_all.sort(key=lambda item: (item.requested - item.submitted,
                                 item.average_latency))

    return h_all[0]


def dijkstra_schedule_smalls(small_queries, graph):
    h = Schedule()
    for sq in small_queries:
        h.requested += sq.bandwidth
        path = dijkstra_route(graph, sq.source, sq.dest, h)
        if path is not None:
            h.submitted += sq.bandwidth
            latency = path[0].get('t')
            if latency > sq.mainq.latency:
                sq.mainq.latency = latency
            for e in reversed(path):
                h.write_one(e.get('s'), e.get('d'), e.get('t'), sq)

    return h


def accurate_solution(queries, graph):
    h_result = None
    l_max = math.inf
    submitted_max = 0
    big_queries = []
    sub_queries = []
    buf_p = 1

    for i in range(len(queries)):
        q = queries[i]
        s = q.get('s')
        d = q.get('d')
        b = q.get('b')
        big_q = Query(s, d, b, 100, i)
        big_q.sub_index = 0
        big_queries.append(big_q)
        for j in range(len(big_q.subq)):
            sub_queries.append(i)
        buf_p *= math.factorial(len(big_q.subq))

    perms = set(itertools.permutations(sub_queries, r = len(sub_queries)))
    for perm in perms:
        sum_latency = 0
        sub_queries = []
        for i in perm:
            big_q = big_queries[i]
            sub_queries.append(big_q.subq[big_q.sub_index])
            big_q.sub_index += 1
        h = dijkstra_schedule_smalls(sub_queries, graph)
        for big_q in big_queries:
            sum_latency += big_q.latency
            if h.max_latency < big_q.latency:
                h.max_latency = big_q.latency
            big_q.latency = 0
            big_q.sub_index = 0

        h.average_latency = sum_latency/len(big_queries)
        if h.submitted > submitted_max:
            h_result = h
            submitted_max = h.submitted
            l_max = h.max_latency
        elif h.submitted == submitted_max:
            if h.max_latency < l_max:
                h_result = h
                l_max = h.max_latency

    return h_result







