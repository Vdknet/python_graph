from task import find_comp
from structures.simple import Edge
from random import randint


adjacency_list = [[1, 2, 4],
                  [2, 3, 4],
                  [0],
                  [],
                  [5],
                  [],
                  [7],
                  []
                 ]


print(find_comp(adjacency_list))

adjacency_list = [[1, 2, 4],
                  [0, 2, 3, 4],
                  [0, 1],
                  [1],
                  [0, 1],
                  [],
                 ]

print(find_comp(adjacency_list))


