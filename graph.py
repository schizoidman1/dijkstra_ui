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
        distancia_caminhada = {node: float('inf') for node in self.G} # Marca todos os nós como infinito
        distancia_caminhada[start_node] = 0 # Marca o nó inicial como 0

        predecessors = {node: None for node in self.G} # Nós predecessores

        fila_de_prioridade = [(0, start_node)] # Criação de uma fila de prioridade utilizando Heap !
        heapq.heapify(fila_de_prioridade)

        while fila_de_prioridade:
            distancia_atual, node_atual = heapq.heappop(fila_de_prioridade)

            if distancia_atual > distancia_caminhada[node_atual]:
                continue

            for vizinho, peso in self.G[node_atual].items():
                distancia = distancia_atual + peso

                if distancia < distancia_caminhada[vizinho]:
                    distancia_caminhada[vizinho] = distancia
                    predecessors[vizinho] = node_atual
                    heapq.heappush(fila_de_prioridade, (distancia, vizinho))

        caminho = []
        node_atual = end_node
        while node_atual:
            caminho.insert(0, node_atual)
            node_atual = predecessors[node_atual]

        if caminho[0] != start_node:
            return None
        
        return caminho, distancia_caminhada[node_atual]

    def plot_graph(self):
        import matplotlib.pyplot as plt
        import networkx as nx
        
        G = nx.DiGraph()
        for start_node, neighbors in self.G.items():
            for end_node, weight in neighbors.items():
                G.add_edge(start_node, end_node, weight=weight)
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="green", font_size=10, font_color="black", font_weight="bold")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

