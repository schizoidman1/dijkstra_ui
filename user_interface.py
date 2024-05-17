from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from graph import Graph
import networkx as nx
import sys

class DijkstraGraphApp(QWidget):
    def __init__(self):
        super().__init__()

        self.graph = Graph()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dijkstra Graph Visualizer')
        self.setGeometry(100, 100, 600, 800)

        icon_path = 'icon.png'
        self.setWindowIcon(QIcon(icon_path))

        self.label_start = QLabel('Nó Inicial:', self)
        self.start_node_input = QLineEdit(self)
        
        self.label_end = QLabel('Nó de Destino:', self)
        self.end_node_input = QLineEdit(self)
        
        self.label_weight = QLabel('Peso da Aresta:', self)
        self.weight_input = QLineEdit(self)

        self.add_edge_button = QPushButton('Add Edge', self)
        self.delete_edge_button = QPushButton('Delete Edge', self)
        self.dijkstra_button = QPushButton('Dijkstra', self)
        self.clear_button = QPushButton('Clear', self)

        self.text_output = QTextEdit(self)
        self.text_output.setReadOnly(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_start)
        self.layout.addWidget(self.start_node_input)
        self.layout.addWidget(self.label_end)
        self.layout.addWidget(self.end_node_input)
        self.layout.addWidget(self.label_weight)
        self.layout.addWidget(self.weight_input)
        self.layout.addWidget(self.add_edge_button)
        self.layout.addWidget(self.delete_edge_button)
        self.layout.addWidget(self.dijkstra_button)
        self.layout.addWidget(self.clear_button)
        self.layout.addWidget(self.text_output)
        self.setLayout(self.layout)

        self.add_edge_button.clicked.connect(self.add_edge_func)
        self.delete_edge_button.clicked.connect(self.delete_edge_func)
        self.dijkstra_button.clicked.connect(self.dijkstra_func)
        self.clear_button.clicked.connect(self.clear_func)

        # Adiciona um widget do matplotlib para exibir o gráfico
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def add_edge_func(self):
        """Adiciona uma aresta ao grafo"""
        start_node = self.start_node_input.text()
        end_node = self.end_node_input.text()
        weight = self.weight_input.text()

        if start_node and end_node and weight:
            try:
                weight = float(weight)
                self.graph.add_edge(start_node, end_node, weight)
                self.text_output.append(f'Adicionada aresta: {start_node} -> {end_node} com peso {weight}')
                self.update_canvas()
                self.start_node_input.clear()
                self.end_node_input.clear()
            except ValueError:
                self.text_output.append('Peso inválido. Por favor, insira um número')
        else:
            self.text_output.append('Por favor, insira valores para todos os campos')

    def delete_edge_func(self):
        """Remove uma aresta do grafo"""
        start_node = self.start_node_input.text()
        end_node = self.end_node_input.text()

        if start_node and end_node:
            self.graph.remove_edge(start_node, end_node)
            self.text_output.append(f'Removida aresta: {start_node} -> {end_node}')
            self.update_canvas()
        else:
            self.text_output.append('Por favor, insira valores para os nós inicial e de destino.')

    def dijkstra_func(self):
        """Executa o algoritmo de Dijkstra"""
        start_node = self.start_node_input.text()
        end_node = self.end_node_input.text()

        if start_node and end_node:
            path = self.graph.dijkstra(start_node, end_node)
            peso = path[1]
            if path:
                self.text_output.append(f'Caminho mais curto de {start_node} para {end_node}: {path[0]} | peso: {peso}')
                self.graph.atualizar_grafo(path)
                self.update_canvas()
            else:
                self.text_output.append(f'Não foi possível encontrar um caminho de {start_node} para {end_node}')
        else:
            self.text_output.append('Por favor, insira valores para os nós inicial e de destino.')

    def clear_func(self):
        """Limpa a visualização do grafo e o texto de saída"""
        self.graph = Graph()
        self.text_output.clear()
        self.figure.clear()
        self.canvas.draw()
        self.text_output.append('Tela limpa')

    def update_canvas(self):
        """Atualiza o canvas do matplotlib com a visualização atual do grafo"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        G = nx.DiGraph()
        for start_node, neighbors in self.graph.G.items():
            for end_node, weight in neighbors.items():
                G.add_edge(start_node, end_node, weight=weight)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_color="black", font_weight="bold", ax=ax)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
        self.canvas.draw()

