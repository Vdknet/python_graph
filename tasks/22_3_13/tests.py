from task import is_single_connected
from structures.simple import Edge
from random import randint


adjacency_list = [[1],
                  [2, 3, 4],
                  [],
                  [],
                  [5],
                  [],
                  [7],
                  []
                 ]


print(is_single_connected(adjacency_list))

adjacency_list = [[1, 2, 4],  
                  [0, 2, 3, 4],
                  [0, 1],
                  [1],
                  [0, 1],
                  [],
                 ]

print(is_single_connected(adjacency_list))


