import heapq

def dijkstra(start_node: str, end_node: str):
    dijkstra = {node: float('inf') for node in self.G}
    dijkstra[start_node] = 0

    predecessores = {node:None for node in self.G}

    fila = [(0, start_node)]

    heapq.heapify(fila)

    while fila:
        peso, no = heapq.heapop(fila)
        
        for vizinho, peso_vizinho in self.G[no].items():
            distancia = peso + peso_vizinho

            if distancia < dijkstra[vizinho]:
                dijkstra[vizinho] = distancia
                predecessores[vizinho] = no
                heapq.heappush(fila, (distancia, vizinho))

    caminho = []
    no_final = end_node

    while no_final
        caminho.insert(no_final)
        no_final = predecessores[no_final]

