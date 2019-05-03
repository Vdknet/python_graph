from algorithms.dfs.dfs import dfs
from structures.simple import Edge
from random import randint


adjacency_list = [[1, 2, 4],
                  [2, 3, 4],
                  [],
                  [],
                  [5],
                  [],
                  [7],
                  []
                 ]
source = 3


print(dfs(adjacency_list, source))


new_adj_list = []

for i in range(len(adjacency_list)):
    new_adj_list.append([])
    for j in range(len(adjacency_list[i])):
        new_adj_list[i].append(Edge(adjacency_list[i][j], randint(0, 9)))

source = 3

print(dfs(new_adj_list, source))

