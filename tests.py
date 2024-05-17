a = {
    'A': {
        'B': 1, 
        'C': 4
        }, 
    'B': {
        'D': 2, 
        'E': 5
        }, 
    'C': {
        'F': 3
        }, 
    'D': {}, 
    'E': {
        'F': 1
        }, 
    'F': {}
}

from graph import Graph

g = Graph()

g.add_edge(start_node='A', end_node='B', weight=10)

path = g.dijkstra('A', 'B')

print(path[1])