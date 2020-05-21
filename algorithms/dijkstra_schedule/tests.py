from algorithms.dijkstra_schedule.dijsktra_schedule import dijkstra_schedule

adjacency_list = [[1, 2, 4],
                  [2, 3],
                  [3, 4, 5],
                  [6],
                  [5],
                  [6],
                  []
                 ]

queries = [{'s': 0, 'd': 6, 'b': 300},
           {'s': 5, 'd': 1, 'b': 150},
           {'s': 4, 'd': 3, 'b': 400}]


schedule = dijkstra_schedule(queries, adjacency_list)
for q in schedule.keys():
    print(q, schedule.get(q))
print(schedule)

print('==================================')

adjacency_list = [[1, 2, 3],
                  [4, 10],
                  [4, 5],
                  [5, 7],
                  [6],
                  [6, 8, 9],
                  [10],
                  [8],
                  [],
                  [10],
                  []
                 ]

queries = [{'s': 7, 'd': 10, 'b': 250},
           {'s': 2, 'd': 6, 'b': 1000},
           {'s': 0, 'd': 4, 'b': 1000},
           {'s': 8, 'd': 1, 'b': 400},
           {'s': 0, 'd': 6, 'b': 300},
           {'s': 5, 'd': 1, 'b': 150},
           {'s': 4, 'd': 3, 'b': 400}]


schedule = dijkstra_schedule(queries, adjacency_list)
for q in schedule.keys():
    print(q, schedule.get(q))
print(schedule)
