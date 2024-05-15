from graph import Graph

graph = Graph()

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'D', 2)
graph.add_edge('B', 'E', 5)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 1)

print(graph.G)
graph.plot_graph()