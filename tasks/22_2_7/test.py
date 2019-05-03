from task import bfs_double_colouring, list_to_node_list


duel_list = [[2, 4],
             [2, 4],
             [0, 1],
             [5, 6],
             [0, 1],
             [3, 6],
             [3, 5]
             ]


result = bfs_double_colouring(list_to_node_list(duel_list), 0)
print(result)

