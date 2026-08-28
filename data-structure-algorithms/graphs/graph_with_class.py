"""
Structure de données : Graphe

Implémenté d'un graphe cyclique non orienté à l'aide de classes
"""

class Graph:
    "Représentation d'un graphe"
    def __init__(self, size: int) -> None:
        self.vertices = [''] * size
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size


    def add_vertex(self, vertex: int, data: str) -> None:
        """
        Ajoute un sommet au graphe

        Args:
            vertex (int): L'indice du sommet à ajouter
            data (str): La valeur du sommet
        """
        if 0 <= vertex < self.size:
            self.vertices[vertex] = data


    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        Ajoute une arête au graphe

        Args:
            from_vertex (int): L'indice du sommet de départ
            to_vertex (int): L'indice du sommet d'arrivée
        """
        if 0 <= from_vertex < self.size and 0 <= to_vertex < self.size:
            self.matrix[from_vertex][to_vertex] = 1
            self.matrix[to_vertex][from_vertex] = 1


    def display_graph(self) -> None:
        """
        Affiche le graphe
        """
        print("\nVoici les connexions pour chaqu'un des sommets:")
        for vertex, _ in enumerate(self.vertices):
            print(f"\n{self.vertices[vertex]}", end=" -> ")
            for connection, _ in enumerate(self.matrix[vertex]):
                if self.matrix[vertex][connection]:
                    print(self.vertices[connection], end=" ")
        print()


graph = Graph(4)

graph.add_vertex(0, "A")
graph.add_vertex(1, "B")
graph.add_vertex(2, "C")
graph.add_vertex(3, "D")

graph.add_edge(0, 1)  # A - B
graph.add_edge(0, 2)  # A - C
graph.add_edge(0, 3)  # A - D
graph.add_edge(1, 2)  # B - C

graph.display_graph()
