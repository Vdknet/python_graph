from algorithms.dfs.dfs import dfs
from structures.simple import Edge
from random import randint


adjacency_list = [[1, 2, 4],
                  [0, 2, 3, 4],
                  [0, 1],
                  [1],
                  [0, 1, 5],
                  [0],
                 ]
source = 3


for i in dfs(adjacency_list, source):
    print(i)

print()

new_adj_list = []

for i in range(len(adjacency_list)):
    new_adj_list.append([])
    for j in range(len(adjacency_list[i])):
        new_adj_list[i].append(Edge(adjacency_list[i][j], randint(0, 9)))

source = 3

for i in dfs(new_adj_list, source):
    print(i)
