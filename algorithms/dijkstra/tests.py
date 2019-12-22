from algorithms.dijkstra.dijkstra import dijkstra

adjacency_list = [{1: 3,
                   2: 2,
                   4: 6},
                  {2: 4,
                   3: 3},
                  {3: 2,
                   4: 1,
                   5: 3},
                  {6: 1},
                  {5: 3},
                  {6: 1},
                  {}
                 ]
source = 0


result = dijkstra(adjacency_list, source)
for node in result:
    print(node.index, node.d)