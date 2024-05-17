import matplotlib.pyplot as plt
import networkx as nx
import heapq


class Graph:
    def __init__(self):
        self.G = {}
    
    def add_edge(self, start_node: str, end_node: str, weight: float):
        if start_node not in self.G:
            self.G[start_node] = {}
        if end_node not in self.G:
            self.G[end_node] = {}
        self.G[start_node][end_node] = weight
    
    def remove_edge(self, start_node: str, end_node: str):
        if start_node in self.G and end_node in self.G[start_node]:
            del self.G[start_node][end_node]
    
    def add_node(self, node: str):
        if node not in self.G:
            self.G[node] = {}
    
    def remove_node(self, node: str):
        if node in self.G:
            del self.G[node]
        for neighbors in self.G.values():
            if node in neighbors:
                del neighbors[node]
    
    def get_neighbors(self, node: str):
        return self.G[node] if node in self.G else {}
   
    def dijkstra(self, start_node: str, end_node: str):
        dijkstra = {node: float('inf') for node in self.G}
        dijkstra[start_node] = 0

        predecessores = {node:None for node in self.G}

        fila = [(0, start_node)]

        heapq.heapify(fila)

        while fila:
            peso, no = heapq.heappop(fila)
            
            for vizinho, peso_vizinho in self.G[no].items():
                distancia = peso + peso_vizinho


                if distancia < dijkstra[vizinho]:
                    dijkstra[vizinho] = distancia
                    predecessores[vizinho] = no
                    heapq.heappush(fila, (distancia, vizinho))

        caminho = []
        no_final = end_node

        while no_final:
            caminho.insert(0, no_final)
            no_final = predecessores[no_final]

        return caminho

    def atualizar_grafo(self, caminho):
        novo_grafo = {}
        for node in caminho:
            novo_grafo[node] = {}
        for i in range(len(caminho) - 1):
            novo_grafo[caminho[i]][caminho[i+1]] = self.G[caminho[i]][caminho[i+1]]
        self.G = novo_grafo

    def plot_graph(self):
        G = nx.DiGraph()
        for start_node, neighbors in self.G.items():
            for end_node, weight in neighbors.items():
                G.add_edge(start_node, end_node, weight=weight)
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="green", font_size=10, font_color="black", font_weight="bold")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

