from task import dfs
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


